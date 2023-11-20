FROM debian:buster-slim

RUN apt-get update && \
    apt-get install -y lib32z1 xinetd default-jdk dos2unix && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN useradd -m user && \
    chown -R root:root /home/user

ENV LANG=C.UTF-8
ADD app /home/user/
RUN javac -encoding utf8 -d /home/user /home/user/Cantstop.java
COPY xinetd /etc/xinetd.d/user
RUN dos2unix /etc/xinetd.d/user

WORKDIR /home/user

EXPOSE 10000

CMD ["/usr/sbin/xinetd", "-dontfork"]
