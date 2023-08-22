FROM python:3.9-slim-buster

RUN apt-get update && \
    pip3 install flask

RUN useradd -m user && \
    chown -R root:root /home/user

ENV LANG=C.UTF-8

ADD src /home/user/

WORKDIR /home/user

EXPOSE 10003

CMD ["/usr/local/bin/python", "/home/user/app.py"]
