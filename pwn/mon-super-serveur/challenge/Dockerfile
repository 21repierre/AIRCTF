from ubuntu:jammy

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && \
	apt install -y gcc

RUN useradd user

WORKDIR /home/user

COPY src/ .
RUN gcc -o main main.c -pthread -Wl,-z,norelro -no-pie -fno-stack-protector
RUN chown -R user:user . && \
chmod -R 700 . && \
chmod +x main

CMD /home/user/main