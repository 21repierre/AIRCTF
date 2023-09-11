FROM debian:buster-slim

RUN apt-get update && \
    apt-get install -y lib32z1 xinetd gcc dos2unix && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m user && \
    chown -R root:root /home/user

ENV LANG=C.UTF-8

ADD src /home/user/
RUN gcc /home/user/keygen.c -o /home/user/keygen -O2 && \
    strip --strip-all /home/user/keygen

COPY xinetd /etc/xinetd.d/user
RUN dos2unix /etc/xinetd.d/user

WORKDIR /home/user

EXPOSE 10002

CMD ["/usr/sbin/xinetd", "-dontfork"]
