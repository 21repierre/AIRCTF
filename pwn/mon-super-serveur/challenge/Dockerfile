from ubuntu:jammy

RUN apt update && \
	apt install -y gcc nano

RUN useradd user

WORKDIR /home/user

COPY src/ .
RUN gcc -o main main.c -Wl,-z,norelro -no-pie -fno-stack-protector
RUN chown -R user:user . && \
chmod -R 700 . && \
chmod +x main


CMD ["cat", "/dev/zero"]
#CMD /home/user/main