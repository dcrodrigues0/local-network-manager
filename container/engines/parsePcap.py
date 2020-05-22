import dpkt
import socket
import datetime
from dpkt.compat import compat_ord
from container.services.sniffer import storage as st
from container.util import util
from collections import Counter

storage = st.Storage()


def parse(fileCap):
    packets_length = 0
    packets_count = 0
    timestampArray = []
    listTraffic = []
    hourTraffic = {}
    ips_destination = []
    ips_source = []
    traffic_table = []
    for ts, buf in fileCap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            proto = ip.data

            timestamp = str(datetime.datetime.fromtimestamp(ts))
            timestampArray = util.timestampFormat(timestamp)
            packets_count += 1
            packets_length += ip.len

            source_ip = util.replace_ip_string(inet_to_str(ip.src))
            destination_ip = util.replace_ip_string(inet_to_str(ip.dst))

            ips_source.append(source_ip)
            ips_destination.append(destination_ip)

            protocol = ip.get_proto(ip.p).__name__
            source_port = proto.sport
            destination_port = proto.dport

            table_record = {"Source-IP": str(source_ip) + ":" + str(source_port),
                            "Destination-IP": str(destination_ip) + ":" + str(destination_port),
                            "Protocol": protocol, "Length": ip.len, "TTL": ip.ttl}
            traffic_table.append(table_record)
        except:
            pass

    dateMonthDat = timestampArray[2] + "-" + timestampArray[1]

    realtime_info = {"min": timestampArray[4], "quantidade_pacotes": packets_count, "date": dateMonthDat}

    hourTraffic = {"hour": timestampArray[3], "quantidade_pacotes": packets_count, "date": dateMonthDat}

    intraday = {'date': dateMonthDat, 'tamanho_pacotes': packets_length, 'quantidade_pacotes': packets_count,
                'avg': util.formatFloat(packets_length / packets_count)}

    trafficMac = {'date': dateMonthDat,
                  'mac_origem': generate_mac_addr(eth.src),
                  'quantidade_pacotes': packets_count}

    traffic_ip_address = {"date": dateMonthDat, "hour": timestampArray[3],
                          "Source-IPs": Counter(ips_source), "Destination-IPs": Counter(ips_destination)}

    realtime_table = {"date": dateMonthDat, "hour": timestampArray[3], "min": timestampArray[4],
                      "Traffic": traffic_table}

    print()
    print("---------------------------")
    print()
    savetTraffic(intraday, hourTraffic, trafficMac, realtime_info, traffic_ip_address, realtime_table, storage)


def savetTraffic(intraday, hourTraffic, trafficMac, realtime_info, traffic_ip, trafficTable, storage):
    storage.storageAll(trafficIntraday=intraday, hourTraffic=hourTraffic, trafficMac=trafficMac,
                       realTimeTraffic=realtime_info, trafficIpAddress=traffic_ip, realTimeTable=trafficTable)


def generate_mac_addr(address):
    # Generate mac address
    # address (str): a MAC address in hex form (e.g. '\x01\x02\x03\x04\x05\x06')
    return ':'.join('%02x' % compat_ord(b) for b in address)


def inet_to_str(inet):
    # First try ipv4 and then ipv6
    try:
        return socket.inet_ntop(socket.AF_INET, inet)
    except ValueError:
        return socket.inet_ntop(socket.AF_INET6, inet)
