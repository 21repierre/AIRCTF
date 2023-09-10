import os

from flask import session, redirect, g
from flask_dance.consumer import OAuth2ConsumerBlueprint

from CTFd import utils
from CTFd.models import db, Users
from CTFd.utils import set_config
from CTFd.utils.logging import log
from CTFd.utils.security.auth import login_user


def load(app):
    ########################
    # Plugin Configuration #
    ########################
    authentication_url_prefix = "/auth"
    oauth_client_id = utils.get_app_config('OAUTHLOGIN_CLIENT_ID')
    oauth_client_secret = utils.get_app_config('OAUTHLOGIN_CLIENT_SECRET')
    oauth_provider = 'cerbair'
    create_missing_user = True

    ##################
    # User Functions #
    ##################
    def retrieve_user_from_database(email):
        user = Users.query.filter_by(email=email).first()
        if user is not None:
            log('logins', "[{date}] {ip} - " + user.name + " - OAuth2 bridged user found")
            return user

    def create_user(email, displayName):
        with app.app_context():
            user = Users(email=email, name=displayName.strip())
            log('logins', "[{date}] {ip} - " + user.name + " - No OAuth2 bridged user found, creating user")
            db.session.add(user)
            db.session.commit()
            db.session.flush()
            return user

    def create_or_get_user(email, displayName):
        user = retrieve_user_from_database(email)
        if user is not None:
            return user
        if create_missing_user:
            return create_user(email, displayName)

    ##########################
    # Provider Configuration #
    ##########################
    def make_cerbair_blueprint():
        bp = OAuth2ConsumerBlueprint(
            "cerbair", __name__,
            client_id=oauth_client_id,
            client_secret=oauth_client_secret,
            base_url="https://cerbair.etu.imt-nord-europe.fr",
            token_url="https://cerbair.etu.imt-nord-europe.fr/api/oauth2/token",
            authorization_url="https://cerbair.etu.imt-nord-europe.fr/api/oauth2/authorize",
            redirect_url=authentication_url_prefix + "/cerbair/confirm",
            scope='email profile',
            token_url_params={'include_client_id': True}
        )

        @bp.before_app_request
        def set_applocal_session():
            g.flask_dance_cerbair = bp.session

        return bp

    provider_blueprints = {
        'cerbair': lambda: make_cerbair_blueprint(),
    }

    def get_cerbair_user():
        user_info = g.flask_dance_cerbair.get("/api/users/@self").json()
        return create_or_get_user(
            email=user_info["email"],
            displayName=user_info["uid"])

    provider_users = {
        'cerbair': lambda: get_cerbair_user(),
    }

    provider_blueprint = provider_blueprints[oauth_provider]()  # Resolved lambda

    #######################
    # Blueprint Functions #
    #######################
    @provider_blueprint.route('/<string:auth_provider>/confirm', methods=['GET'])
    def confirm_auth_provider(auth_provider):
        if not auth_provider in provider_users:
            return redirect('/')

        provider_user = provider_users[oauth_provider]()
        session.regenerate()

        if provider_user is not None:
            login_user(provider_user)

        return redirect('/')

    app.register_blueprint(provider_blueprint, url_prefix=authentication_url_prefix)

    ###############################
    # Application Reconfiguration #
    ###############################
    # ('', 204) is "No Content" code
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    set_config('registration_visibility', False)
    app.view_functions['auth.login'] = lambda: redirect(authentication_url_prefix + "/" + oauth_provider)
    app.view_functions['auth.register'] = lambda: ('', 204)
    app.view_functions['auth.reset_password'] = lambda: ('', 204)
    app.view_functions['auth.confirm'] = lambda: ('', 204)
