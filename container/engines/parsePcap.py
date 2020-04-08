import dpkt
import socket
import datetime
from dpkt.compat import compat_ord

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

def parse(fileCap):
    for ts, buf in fileCap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)

            do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
            more_fragments = bool(ip.off & dpkt.ip.IP_MF)
            fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

            dataFormat = {'timestamp': str(datetime.datetime.utcfromtimestamp(ts)), 'mac_origem':generate_mac_addr(eth.src), 'mac_destino':generate_mac_addr(eth.dst),
                          'ip_origem': inet_to_str(ip.src), 'ip_destino': inet_to_str(ip.dst), 'packet_size': ip.len}

            print(dataFormat)
        except:
            pass


