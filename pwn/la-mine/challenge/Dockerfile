FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y lib32z1 xinetd dos2unix && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m user && \
    chown -R root:root /home/user

ENV LANG=C.UTF-8

ADD src /home/user/
RUN chmod +x /home/user/start.sh
RUN chmod +x /home/user/main

COPY xinetd /etc/xinetd.d/user
RUN dos2unix /etc/xinetd.d/user

WORKDIR /home/user

EXPOSE 10006

CMD ["/usr/sbin/xinetd", "-dontfork"]
