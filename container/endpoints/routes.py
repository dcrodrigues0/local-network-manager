from flask import Blueprint
from flask import request
from container.services.sniffer import service
from container.services.admin import admin

routes = Blueprint('simple_page', __name__, template_folder='templates')
service = service.Service()


@routes.route('/')
def hello():
    name = request.args.get('name', '')
    return "Hello World" + name


@routes.route('/date')
def intraday():
    try:
        return responseData("success", 200, service.getTrafficByDate(request.args.get('date', 00)))
    except:
        return responseData("error", 500, [])


@routes.route('/date/hour')
def traffic_hour():
    try:
        return responseData("success", 200, service.getTrafficHourByDate(request.args.get('date', 00)))
    except:
        return responseData("error", 500, [])


@routes.route('/ip-addresses/src')
def ip_addresses_traffic():
    try:
        date = request.args.get('date')
        hour = request.args.get('hour')
        return responseData("success", 200, service.getIpTrafficSrc(date, hour))
    except:
        return responseData("error", 500, [])


# --------------ADMIN----------------
@routes.route('/admin/process')
def execProcess():
    admin.startProcess()
    return responseSuccess()


# -----RESPONSE --------
def responseSuccess():
    return {"Message": "Success", "Status": 200}


def responseData(message, status, data):
    return {"Message": message, "Status": status, "data": data}
