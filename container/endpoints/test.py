from flask import Blueprint
from flask import request

test = Blueprint('simple_page', __name__, template_folder='templates')
@test.route('/')
def hello():
    name = request.args.get('name','')
    return 'Bem vindo ' + name