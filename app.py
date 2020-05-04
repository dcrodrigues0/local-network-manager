from flask import Flask
from container.endpoints.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)
