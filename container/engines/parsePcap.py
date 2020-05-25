import dpkt
import socket
import datetime
from dpkt.compat import compat_ord

import container.helper.ip_address
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

            proto = ip.data if hasattr(ip, 'data') else None
            protocol = ip.get_proto(ip.p).__name__ if hasattr(ip, 'get_proto') else None

            source_ip = None
            source_port = None
            destination_ip = None
            destination_port = None
            length = None
            ttl = None

            timestamp = str(datetime.datetime.fromtimestamp(ts))
            timestampArray = util.timestampFormat(timestamp)
            packets_count += 1

            if eth.type == dpkt.ethernet.ETH_TYPE_ARP:

                protocol = "ARP"
                source_ip = container.helper.ip_address.replace_ip_string(inet_to_str(ip.spa))
                destination_ip = container.helper.ip_address.replace_ip_string(inet_to_str(ip.tpa))
                length = ip.pln

            elif eth.type == dpkt.ethernet.ETH_TYPE_IP:

                packets_length += ip.len
                source_ip = container.helper.ip_address.replace_ip_string(inet_to_str(ip.src))
                destination_ip = container.helper.ip_address.replace_ip_string(inet_to_str(ip.dst))
                source_port = proto.sport if hasattr(proto, 'sport') else None
                destination_port = proto.dport if hasattr(proto, 'dport') else None
                length = ip.len
                ttl = ip.ttl

            elif eth.type == dpkt.ethernet.ETH_TYPE_IP6:

                packets_length += ip.plen
                source_ip = socket.inet_ntop(socket.AF_INET6, ip.src)
                destination_ip = socket.inet_ntop(socket.AF_INET6, ip.dst)
                source_port = proto.sport if hasattr(proto, 'sport') else None
                destination_port = proto.dport if hasattr(proto, 'dport') else None
                length = ip.plen
                ttl = ip.hlim

            if source_ip is not None: ips_source.append(source_ip)
            if destination_ip is not None: ips_destination.append(destination_ip)

            table_record = {"Source-IP": str(source_ip), "Source-Port": source_port,
                            "Destination-IP": str(destination_ip), "Destination-Port": destination_port,
                            "Protocol": protocol, "Length": length, "TTL": ttl}

            traffic_table.append(table_record)
        except Exception as e:
            print(e)

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
