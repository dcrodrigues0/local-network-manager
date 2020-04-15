# local-network-manager

- It is a network manager to domestic networks, with our project you will can do simples managements and keep up what's happening in your domestic networks.


# How to run
 1. We did our project using <a href="https://www.jetbrains.com/pycharm/download/">PyCharm IDE</a> so you also should use <a href="https://www.jetbrains.com/pycharm/download/">PyCharm</a> to don't get problems, but be free ;)
 2. You must to install the dependencies, you can find the dependencies below.
 3. Run MongoDB with docker in the root folder example: `docker-compose up -d`
 4. After that, you can run our server using `FLASK_APP=app.py flask run`,or if you prefer can see more examples of how to start a Flask server at <a href="https://github.com/pallets/flask">Flask Documentation</a>

# Dependencies
 - `Flask` <a href="https://github.com/pallets/flask/">Flask Docs</a>
 - `Pyshark` <a href="https://kiminewt.github.io/pyshark/">Pyshark Docs</a>
 - `Docker` <a href="https://www.docker.com/">Docker Docs</a>
 - `Pymongo` <a href="https://api.mongodb.com/python/current/tutorial.html">Pymongo Docs</a>
 
# Build
 
1 - Install required packages
- `sudo apt-get install npm nodejs docker docker-compose python3 python-pip -y`
 
2 - Install python dependencies
- `pip install -r requirements.txt --user`

3 - Install front end dependencies
- cd ./front-py-network/
- `npm install`

4 - Build docker image on root folder
- `docker-compose up --build`

5 - Start Vue Cli Server
- cd ./front-py-network/
- `npm start`

URL Access:
- http://localhost:8080/