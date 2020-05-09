from flask import Flask
from container.endpoints.routes import routes
from dotenv import load_dotenv
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)


app.register_blueprint(routes)
load_dotenv()

