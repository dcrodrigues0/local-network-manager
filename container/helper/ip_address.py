def replace_ip_string(str1, replace_dots=True):
    if replace_dots is False:
        return str1.replace('/', '.')
    else:
        return str1.replace('.', '/')


def add_new_ips(ips, packets):
    for ip_address, quantity_packets in packets["Source-IPs"].copy().items():
        if ip_address not in ips["Source-IPs"].keys():
            ips["Source-IPs"][ip_address] = quantity_packets
            del (packets["Source-IPs"][ip_address])

    for ip_address, quantity_packets in ips["Source-IPs"].items():
        if ip_address in packets["Source-IPs"]:
            ips["Source-IPs"][ip_address] += packets["Source-IPs"][ip_address]

    for ip_address, quantity_packets in packets["Destination-IPs"].copy().items():
        if ip_address not in ips["Destination-IPs"].keys():
            ips["Destination-IPs"][ip_address] = quantity_packets
            del (packets["Destination-IPs"][ip_address])

    for ip_address, quantity_packets in ips["Destination-IPs"].items():
        if ip_address in packets["Destination-IPs"]:
            ips["Destination-IPs"][ip_address] += packets["Destination-IPs"][ip_address]

    return ips
