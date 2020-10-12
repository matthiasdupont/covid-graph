#FROM ubuntu:18.04
FROM python:rc-slim

RUN apt-get update
#install curl for test purpose
#RUN apt-get -y install curl
#RUN apt-get -y install python3
#RUN apt-get -y install python3-pip
RUN pip3 install bottle
RUN apt-get -y install git
# creation du repertoire applicatif (mkdir + cd)
WORKDIR /opt/app
COPY . .
ENTRYPOINT /bin/bash -c "python3 app.py"
