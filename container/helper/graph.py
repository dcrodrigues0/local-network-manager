import container.helper.ip_address


def tones_of_blue():
    return ['powderblue', 'lightblue', 'lightskyblue', 'skyblue', 'deepskyblue', 'lightsteelblue',
            'dodgerblue', 'cornflowerblue',
            'steelblue', 'royalblue', 'blue', 'mediumblue', 'darkblue', 'navy', 'midnightblue',
            'mediumslateblue', 'slateblue', 'darkslateblue', 'lavender', 'gainsboro', 'azure']


def makeDataIpGraph(value, direction, exibition, subtitle):
    ips = value
    ips_dict = ips.next()
    labels = []
    dataset = []
    colorsAvaliable = tones_of_blue()

    colors = []
    i = 0

    for ip, packets in ips_dict[direction].items():
        labels.append(container.helper.ip_address.replace_ip_string(ip, False))
        dataset.append(packets)
        colors.append(colorsAvaliable[i])
        if (i == 20):
            i = 0
        i += 1

    return {'labels': labels,
            'datasets': [{'data': dataset, 'label': subtitle, exibition: 'powderblue',
                          'backgroundColor': 'rgba(176, 224, 230, 0.2)' if exibition == 'borderColor' else colors}]}


def makeDataGraph(value, campoLabel, campoDataset, exibition, subtitle):
    labels = []
    dataset = []
    colorsAvaliable = tones_of_blue()

    colors = []
    i = 0

    for doc in value:
        labels.append(doc[campoLabel])
        dataset.append(doc[campoDataset])
        colors.append(colorsAvaliable[i])
        if i == 20:
            i = 0
        i += 1

    return {'labels': labels,
            'datasets': [{'data': dataset, 'label': subtitle, exibition: 'powderblue',
                          'backgroundColor': 'rgba(176, 224, 230, 0.2)' if exibition == 'borderColor' else colors}]}


def makeDataSubGraph(value, exibition, subtitle):
    labels = []
    dataset = []
    colorsAvaliable = tones_of_blue()

    colors = []
    i = 0

    for doc in value:
        labels.append(container.helper.ip_address.replace_ip_string(doc["ip"], False))
        dataset.append(doc["size"])
        colors.append(colorsAvaliable[i])
        if i == 20:
            i = 0
        i += 1

    return {'labels': labels,
            'datasets': [{'data': dataset, 'label': subtitle, exibition: 'powderblue',
                          'backgroundColor': 'rgba(176, 224, 230, 0.2)' if exibition == 'borderColor' else colors}]}
