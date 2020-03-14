from flask import Flask
from service.NetworkManager import NetworkManager

app = Flask(__name__)

@app.route("/")
def hello():
    network = NetworkManager()
    return "xxxxx"

