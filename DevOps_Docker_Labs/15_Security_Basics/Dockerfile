
FROM ubuntu:latest

RUN useradd -m newuser

USER newuser

COPY 1script.sh /home/newuser/2script.sh

CMD ["bash", "/home/newuser/2script.sh"]
