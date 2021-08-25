FROM ubuntu 
RUN apt-get update 
RUN snap install docker -y
RUN docker run -dit --name Nani ubuntu
