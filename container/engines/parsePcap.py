import dpkt
import socket
import datetime
from dpkt.compat import compat_ord
from container.services.sniffer import storage as st
from container.util import util
from collections import Counter


def parse(fileCap):
    storage = st.Storage()
    packets_length = 0
    packets_count = 0
    timestampArray = []
    listTraffic = []
    hourTraffic = {}
    ips_destination = []
    ips_source = []

    for ts, buf in fileCap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data

            timestamp = str(datetime.datetime.fromtimestamp(ts))
            packets_count += 1
            packets_length += ip.len

            timestampArray = util.timestampFormat(timestamp)

            mac_destino = generate_mac_addr(eth.dst)
            mac_origem = generate_mac_addr(eth.src)

            ips_source.append(util.replace_ip_string(inet_to_str(ip.src)))
            ips_destination.append(util.replace_ip_string(inet_to_str(ip.dst)))

        except:
            pass

    dateMonthDat = timestampArray[2] + "-" + timestampArray[1]
    hourTraffic = {"hour": timestampArray[3], "quantidade_pacotes": packets_count, "date": dateMonthDat}
    intraday = {'date': dateMonthDat, 'tamanho_pacotes': packets_length, 'quantidade_pacotes': packets_count, \
                'avg': util.formatFloat(packets_length / packets_count)}
    packets_by_ip_address_source = {"date": dateMonthDat, "hour": timestampArray[3], "Source-IPs": Counter(ips_source),
                                    "Destination-IPs": Counter(ips_destination)}

    savetTraffic(intraday, hourTraffic, storage, packets_by_ip_address_source)

    day = 0


def savetTraffic(intraday, hourTraffuc, storage, trafficIpSource):
    storage.storageAll(trafficIntraday=intraday, hourTraffic=hourTraffuc, trafficIpSource=trafficIpSource)


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

