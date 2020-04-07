from flask import Flask
from container.endpoints.test import test

app = Flask(__name__)
app.register_blueprint(test)
