from flask import Blueprint

test = Blueprint('simple_page', __name__, template_folder='templates')
@test.route("/")
def hello():
    return "TEste dse endpoint"
