FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get install -y lib32z1 xinetd dos2unix && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m user && \
    chown -R root:root /home/user

ADD app /home/user/
COPY xinetd /etc/xinetd.d/user
RUN dos2unix /etc/xinetd.d/user

WORKDIR /home/user

EXPOSE 9991

CMD ["/usr/sbin/xinetd", "-dontfork"]
