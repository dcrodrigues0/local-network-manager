from flask import Flask
from container.endpoints.routes import routes
from dotenv import load_dotenv

app = Flask(__name__)
app.register_blueprint(routes)
load_dotenv()

