from flask import Blueprint
from flask import request
from container.services.sniffer import service
from container.services.admin import admin

routes = Blueprint('simple_page', __name__, template_folder='templates')
service = service.Service()


@routes.route('/date')
def intraday():
    try:
        exibition = request.args.get('exibition')
        subittle = request.args.get('subittle')

        return responseData("success", 200, service.getTrafficByDate(request.args.get('date', 00), exibition,subittle))
    except:
        return responseData("error", 500, [])


@routes.route('/date/hour')
def traffic_hour():
    try:
        exibition = request.args.get('exibition')
        subittle = request.args.get('subittle')

        return responseData("success", 200, service.getTrafficHourByDate(request.args.get('date', 00),exibition,subittle))
    except:
        return responseData("error", 500, [])


@routes.route('/ipv4/source')
def ipv4_source_traffic():
    try:
        date = request.args.get('date')
        hour = request.args.get('hour')
        exibition = request.args.get('exibition')
        subittle = request.args.get('subittle')

        return responseData("success", 200, service.getTrafficIp(date, hour, "Source-IPs",exibition,subittle))
    except:
        return responseData("error", 500, [])


@routes.route('/ipv4/destination')
def ipv4_destination_traffic():
    try:
        date = request.args.get('date')
        hour = request.args.get('hour')
        exibition = request.args.get('exibition')
        subittle = request.args.get('subittle')

        return responseData("success", 200, service.getTrafficIp(date, hour, "Destination-IPs",exibition,subittle))
    except:
        return responseData("error", 500, [])


@routes.route('/realtime')
def realTime():
    try:
        exibition = request.args.get('exibition')
        subittle = request.args.get('subittle')

        return responseData("success", 200, service.getRealTimeService(exibition,subittle))
    except:
        return responseData("error", 500, [])


@routes.route('/trafficmac')
def trafficmac():
    try:
        exibition = request.args.get('exibition')
        subittle = request.args.get('subittle')

        return responseData("success", 200, service.getTrafficByMacAddress( request.args.get('date', 00),exibition,subittle))
    except:
        return responseData("error", 500, [])


@routes.route('/range')
def trafficRange():
    try:
        exibition = request.args.get('exibition')
        subittle = request.args.get('subittle')
        start = request.args.get('start', 00)
        end = request.args.get('end', 00)

        return responseData("success", 200, service.getTrafficByRange(start, end, exibition,subittle))
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
