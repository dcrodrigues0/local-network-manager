import dpkt
import socket
import datetime
from dpkt.compat import compat_ord
from container.services.job import storage as st

def parse(fileCap):
    process = st.Storage()
    packets_length = 0
    packets_count = 0
    day = 0
    listTraffic = []

    for ts, buf in fileCap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            timestamp = str(datetime.datetime.utcfromtimestamp(ts))

            packets_count+=1
            packets_length+=ip.len

            day = timestamp.split(" ")[0].split("-")[2]
            dataFormat = {'timestamp': timestamp, 'mac_origem':generate_mac_addr(eth.src), 'mac_destino':generate_mac_addr(eth.dst),
                        'ip_origem': inet_to_str(ip.src), 'ip_destino': inet_to_str(ip.dst), 'packet_size': ip.len}

            listTraffic.append(dataFormat)

            #process.storageTraffic(dataFormat)
            #print(dataFormat)
        except:
            pass

    if len(listTraffic) > 0:
        intraday = {'day':day,'tamanho_pacotes':packets_length, 'quantidade_pacotes':packets_count}
        savetTraffic(listTraffic, intraday, process)
        day = 0



def savetTraffic(list, intraday, storage):
    storage.storageAll(trafficFull=list, trafficIntraday=intraday)

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
