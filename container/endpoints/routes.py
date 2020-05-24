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
        subtitle = request.args.get('subtitle')

        return responseData("success", 200, service.getTrafficByDate(request.args.get('date', 00), exibition,subtitle))
    except Exception as e:
        print(e)
        return responseData("error", 500, [])


@routes.route('/date/hour')
def traffic_hour():
    try:
        exibition = request.args.get('exibition')
        subtitle = request.args.get('subtitle')

        return responseData("success", 200, service.getTrafficHourByDate(request.args.get('date', 00),exibition,subtitle))
    except Exception as e:
        print(e)
        return responseData("error", 500, [])


@routes.route('/ipv4/source')
def ipv4_source_traffic():
    try:
        date = request.args.get('date')
        hour = request.args.get('hour')
        exibition = request.args.get('exibition')
        subtitle = request.args.get('subtitle')

        return responseData("success", 200, service.getTrafficIp(date, hour, "Source-IPs",exibition,subtitle))
    except Exception as e:
        print(e)
        return responseData("error", 500, [])


@routes.route('/ipv4/destination')
def ipv4_destination_traffic():
    try:
        date = request.args.get('date')
        hour = request.args.get('hour')
        exibition = request.args.get('exibition')
        subtitle = request.args.get('subtitle')

        return responseData("success", 200, service.getTrafficIp(date, hour, "Destination-IPs",exibition,subtitle))
    except Exception as e:
        print(e)
        return responseData("error", 500, [])


@routes.route('/realtime')
def realTimeGraph():
    try:
        exibition = request.args.get('exibition')
        subtitle = request.args.get('subtitle')

        return responseData("success", 200, service.getRealTimeService(exibition,subtitle))
    except Exception as e:
        print(e)
        return responseData("error", 500, [])

@routes.route('/realtime/table')
def realTimeTable():
    try:
        return responseData("success", 200, service.getRealTimeTrafficTableService())
    except Exception as e:
        print(e)
        return responseData("error", 500, [])

@routes.route('/trafficmac')
def trafficmac():
    try:
        exibition = request.args.get('exibition')
        subtitle = request.args.get('subtitle')

        return responseData("success", 200, service.getTrafficByMacAddress( request.args.get('date', 00),exibition,subtitle))
    except Exception as e:
        print(e)
        return responseData("error", 500, [])


@routes.route('/range')
def trafficRange():
    try:
        exibition = request.args.get('exibition')
        subtitle = request.args.get('subtitle')
        start = request.args.get('start', 00)
        end = request.args.get('end', 00)

        return responseData("success", 200, service.getTrafficByRange(start, end, exibition,subtitle))
    except Exception as e:
        print(e)
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
