
FROM ubuntu:latest

RUN mkdir -p /source /backup
RUN echo "This is file 1" > /source/file1.txt && echo "This is file 2" > /source/file2.txt

CMD cp -r /source/. /backup/
