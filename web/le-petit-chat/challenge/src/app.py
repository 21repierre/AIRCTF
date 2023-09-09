import time
from flask import Flask, request, render_template, send_file
from hashlib import sha1

base_url = 'http://airctf.pierrebdvl.fr:10003'

app = Flask(__name__)
uploads = [
    {
        'filename': 'flag.mp4',
        'exp': 1698578310,
        'sig': '',
        'author': 'admin'
    },
    {
        'filename': 'logo_air.png',
        'exp': 1689568310,
        'sig': '',
        'author': 'AIR'
    },
    {
        'filename': 'flag.txt',
        'exp': 1688558310,
        'sig': '',
        'author': 'admin'
    },
]


@app.route('/file/<string:filename>', methods=['GET'])
def getFile(filename):
    params = request.args
    exp = params.get('exp')
    sig = params.get('sig')
    print(filename, exp, sig)
    if exp is None or sig is None or exp == '' or sig == '':
        return render_template('error.html', message='Missing exp or sig.'), 400
    
    for upload in uploads:
        if upload['filename'] == filename:
            url_sig = request.url.replace(f"&sig={sig}", '').encode()
            url_sig = sha1(url_sig).hexdigest()
            if url_sig == sig:
                if int(exp) > int(time.time()):
                    return send_file(f"files/{upload['filename']}")
                else:
                    return render_template('error.html', message='File has expired.'), 400
            else:
                return render_template('error.html', message='Invalid signature.'), 400

    return render_template('error.html', message='File not found.'), 404

@app.route('/upload', methods=['POST'])
def upload():
    return render_template('error.html', message='Uploads are currently disabled.'), 400

@app.route("/", methods=['GET'])
def home():

    return render_template('index.html', uploads = uploads, now = int(time.time()))


if __name__ == "__main__":
    for upload in uploads:
        url_sig = f"{base_url}/file/{upload['filename']}?exp={upload['exp']}".encode()
        print(url_sig)
        upload['sig'] = sha1(url_sig).hexdigest()
    app.run(host="0.0.0.0", port=10003, debug = True)