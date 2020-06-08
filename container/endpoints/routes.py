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

        return responseData("success", 200, service.getTrafficByDate(request.args.get('date', 00), exibition, subtitle))
    except Exception as e:
        print(e)
        return responseData("error", 500, [])


@routes.route('/date/hour')
def traffic_hour():
    try:
        exibition = request.args.get('exibition')
        subtitle = request.args.get('subtitle')

        return responseData("success", 200,
                            service.getTrafficHourByDate(request.args.get('date', 00), exibition, subtitle))
    except Exception as e:
        print(e)
        return responseData("error", 500, [])

@routes.route('/date/hour/ipv4')
def traffic_hour_ipv4():
    try:
        exibition = request.args.get('exibition')
        subtitle = request.args.get('subtitle')
        date = request.args.get('date')
        hour = request.args.get('hour')

        return responseData("success", 200,
                            service.getHighestIpTrafficByHour(date, hour, exibition, subtitle))
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

        return responseData("success", 200, service.getTrafficIp(date, hour, "Source-IPs", exibition, subtitle))
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

        return responseData("success", 200, service.getTrafficIp(date, hour, "Destination-IPs", exibition, subtitle))
    except Exception as e:
        print(e)
        return responseData("error", 500, [])


@routes.route('/realtime')
def realTimeGraph():
    try:
        exibition = request.args.get('exibition')
        subtitle = request.args.get('subtitle')

        return responseData("success", 200, service.getRealTimeService(exibition, subtitle))
    except Exception as e:
        print(e)
        return responseData("error", 500, [])


@routes.route('/realtime/table')
def realTimeTable():
    try:
        source_ip = request.args.get('src-ip')
        destination_ip = request.args.get('dst-ip')

        source_port = request.args.get('src-port')
        destination_port = request.args.get('dst-port')

        start_src_port = request.args.get('start-src-port')
        end_src_port = request.args.get('end-src-port')

        start_dst_port = request.args.get('start-dst-port')
        end_dst_port = request.args.get('end-dst-port')

        protocol = request.args.get('protocol')

        start_length = request.args.get('start-length')
        end_length = request.args.get('end-length')

        start_ttl = request.args.get('start-ttl')
        end_ttl = request.args.get('end-ttl')

        limit_query = request.args.get('limit')

        date = request.args.get('date')
        hour = request.args.get('hour')

        return responseData("success", 200,
                            service.getRealTimeTrafficTableService(source_ip=source_ip, destination_ip=destination_ip,
                                                                   source_port=source_port,
                                                                   destination_port=destination_port, protocol=protocol,
                                                                   start_length=start_length, end_length=end_length,
                                                                   start_ttl=start_ttl, end_ttl=end_ttl,
                                                                   start_src_port=start_src_port,
                                                                   end_src_port=end_src_port,
                                                                   start_dst_port=start_dst_port,
                                                                   end_dst_port=end_dst_port,
                                                                   limit=limit_query,
                                                                   date=date,
                                                                   hour=hour))
    except Exception as e:
        print(e)
        return responseData("error", 500, [])


@routes.route('/trafficmac')
def trafficmac():
    try:
        exibition = request.args.get('exibition')
        subtitle = request.args.get('subtitle')

        return responseData("success", 200,
                            service.getTrafficByMacAddress(request.args.get('date', 00), exibition, subtitle))
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

        return responseData("success", 200, service.getTrafficByRange(start, end, exibition, subtitle))
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
