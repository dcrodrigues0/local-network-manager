FROM ubuntu:latest
MAINTAINER Docker

WORKDIR /var/www

RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -

RUN sudo apt-get install gnupg

RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -

RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

RUN sudo apt-get update

RUN sudo apt-get install -y mongodb-org

RUN echo "mongodb-org hold" | sudo dpkg --set-selections
RUN echo "mongodb-org-server hold" | sudo dpkg --set-selections
RUN echo "mongodb-org-shell hold" | sudo dpkg --set-selections
RUN echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
RUN echo "mongodb-org-tools hold" | sudo dpkg --set-selections


RUN sudo systemctl status mongod

# Create the MongoDB data directory
RUN mkdir -p /data/db

# Expose port #27017 from the container to the host
EXPOSE 27017

# Set /usr/bin/mongod as the dockerized entry-point application
ENTRYPOINT sudo systemctl daemon-reload
ENTRYPOINT sudo systemctl status mongod