import dpkt
import socket
import datetime
from dpkt.compat import compat_ord
from container.services.sniffer import storage as st
from container.util import util

storage = st.Storage()
def parse(fileCap):

    packets_length = 0
    packets_count = 0
    timestampArray = []
    listTraffic = []
    hourTraffic = {}

    for ts, buf in fileCap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            timestamp = str(datetime.datetime.fromtimestamp(ts))
            packets_count+=1
            packets_length+=ip.len
            timestampArray = util.timestampFormat(timestamp)
            mac_destino = generate_mac_addr(eth.dst)
            mac_origem = generate_mac_addr(eth.src)

        except:
            pass


    dateMonthDat = timestampArray[2] + "-" + timestampArray[1]
    realtime_info = {"min": timestampArray[4], "quantidade_pacotes":packets_count, "date":dateMonthDat}
    hourTraffic = {"hour": timestampArray[3], "quantidade_pacotes": packets_count, "date": dateMonthDat}
    intraday = {'date':dateMonthDat,'tamanho_pacotes':packets_length, 'quantidade_pacotes':packets_count, \
                'avg': util.formatFloat(packets_length/packets_count)}

    trafficMac = {'date': dateMonthDat,
                  'mac_origem': generate_mac_addr(eth.src),
                  'quantidade_pacotes': packets_count}


    print()
    print("---------------------------")
    print()
    savetTraffic(intraday, hourTraffic, trafficMac, realtime_info,storage)

def savetTraffic(intraday, hourTraffic, trafficMac, realtime_info,storage):
    storage.storageAll(trafficIntraday=intraday,  hourTraffic=hourTraffic, trafficMac=trafficMac, realTimeTraffic=realtime_info)

def generate_mac_addr(address):
    #Generate mac address
    #address (str): a MAC address in hex form (e.g. '\x01\x02\x03\x04\x05\x06')
    return ':'.join('%02x' % compat_ord(b) for b in address)


def inet_to_str(inet):
    # First try ipv4 and then ipv6
    try:
        return socket.inet_ntop(socket.AF_INET, inet)
    except ValueError:
        return socket.inet_ntop(socket.AF_INET6, inet)


