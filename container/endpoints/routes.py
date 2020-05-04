from flask import Blueprint
from flask import request
from container.services.sniffer import service
from container.services.admin import admin


routes = Blueprint('simple_page', __name__, template_folder='templates')
service = service.Service()

@routes.route('/')
def hello():
    name = request.args.get('name','')
    return "Hello World" + name

@routes.route('/intraday')
def intraday():
    date = request.args.get('date',00)
    return service.getTrafficByDate(date)



# --------------ADMIN----------------
@routes.route('/admin/process')
def execProcess():
    admin.startProcess()
    return responseSuccess()


#-----RESPONSE --------
def responseSuccess():
    return {"Message": "Success", "Status":200}
