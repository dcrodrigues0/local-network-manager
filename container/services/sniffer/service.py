from container.services.dbutils import mongo
from container.util import util


class Service(mongo.MongoDAO):
    def __init__(self):
        mongo.MongoDAO.__init__(self)

    def getTrafficByDate(self, date, exibition, subtitle):
        return self.makeDataGraph(self.getTrafficByDay(date), 'date', 'avg', exibition, subtitle)

    def getTrafficHourByDate(self, date, exibition, subtitle):
        return self.makeDataGraph(self.getTrafficHour(date), 'hour', 'quantidade_pacotes', exibition, subtitle)

    def getRealTimeService(self, exibition, subtitle):
        return self.makeDataGraph(self.getRealTime(), "min", "quantidade_pacotes", exibition, subtitle)

    def getRealTimeTrafficTableService(self, **Kwargs):
        args = self.createArgumentsinArray(Kwargs)

        Kwargs["limit"] = int(Kwargs["limit"]) if Kwargs["limit"] is not None and int(Kwargs["limit"]) < 500 else 100

        return self.formatTableData(self.getRealTimeTrafficTable(args, Kwargs["limit"]))

    def getTrafficByMacAddress(self, date, exibition, subtitle):
        return self.makeDataGraph(self.getTrafficMac(date), 'mac_origem', 'quantidade_pacotes', exibition, subtitle)

    def getTrafficByRange(self, start, end, exibition, subtitle):

        start = start.split("-")
        end = end.split("-")

        contentField = self.getTrafficBetween()
        traffic = []

        for content in contentField:
            if content["date"].split("-")[1] >= start[1] and content["date"].split("-")[1] <= end[1]:
                if content["date"].split("-")[0] >= start[0] and content["date"].split("-")[0] <= end[0]:
                    traffic.append(content)

        return self.makeDataGraph(traffic, 'date', 'quantidade_pacotes', exibition, subtitle)

    def makeDataGraph(self, value, campoLabel, campoDataset, exibition, subtitle):
        labels = []
        dataset = []
        colorsAvaliable = ['powderblue', 'lightblue', 'lightskyblue', 'skyblue', 'deepskyblue', 'lightsteelblue',
                           'dodgerblue', 'cornflowerblue',
                           'steelblue', 'royalblue', 'blue', 'mediumblue', 'darkblue', 'navy', 'midnightblue',
                           'mediumslateblue', 'slateblue', 'darkslateblue', 'lavender', 'gainsboro', 'azure']
        colors = []
        i = 0

        for doc in value:
            labels.append(doc[campoLabel])
            dataset.append(doc[campoDataset])
            colors.append(colorsAvaliable[i])
            if (i == 20):
                i = 0
            i += 1

        return {'labels': labels,
                'datasets': [{'data': dataset, 'label': subtitle, exibition: 'powderblue',
                              'backgroundColor': 'rgba(176, 224, 230, 0.2)' if exibition == 'borderColor' else colors}]}

    def getTrafficIp(self, date, hour, direction, exibition, subtitle):
        return self.makeDataIpGraph(self.getTrafficIpAddress(date, hour), direction, exibition, subtitle)

    def makeDataIpGraph(self, value, direction, exibition, subtitle):
        ips = value
        ips_dict = ips.next()
        labels = []
        dataset = []
        colorsAvaliable = ['powderblue', 'lightblue', 'lightskyblue', 'skyblue', 'deepskyblue', 'lightsteelblue',
                           'dodgerblue', 'cornflowerblue',
                           'steelblue', 'royalblue', 'blue', 'mediumblue', 'darkblue', 'navy', 'midnightblue',
                           'mediumslateblue', 'slateblue', 'darkslateblue', 'lavender', 'gainsboro', 'azure']
        colors = []
        i = 0

        for ip, packets in ips_dict[direction].items():
            labels.append(util.replace_ip_string(ip, False))
            dataset.append(packets)
            colors.append(colorsAvaliable[i])
            if (i == 20):
                i = 0
            i += 1

        return {'labels': labels,
                'datasets': [{'data': dataset, 'label': subtitle, exibition: 'powderblue',
                              'backgroundColor': 'rgba(176, 224, 230, 0.2)' if exibition == 'borderColor' else colors}]}

    def formatTableData(self, table_collection):
        table_dataset = []

        for record in table_collection:
            record["Traffic"]["Source-IP"] = util.replace_ip_string(record["Traffic"]["Source-IP"], False)
            record["Traffic"]["Destination-IP"] = util.replace_ip_string(record["Traffic"]["Destination-IP"], False)
            table_dataset.append(record)

        return {"dataset": table_dataset}


    def createArgumentsinArray(self, kwargs):
        args = []

        if kwargs.get("source_ip") is not None:
            kwargs["source_ip"] = util.replace_ip_string(kwargs["source_ip"], False)
            args.append({"$regexMatch": {"input": "$$t.Source-IP", "regex": ".*" + kwargs["source_ip"] + ".*"}})

        if kwargs.get("destination_ip") is not None:
            kwargs["destination_ip"] = util.replace_ip_string(kwargs["destination_ip"], False)
            args.append({"$regexMatch": {"input": "$$t.Destination-IP", "regex": ".*" + kwargs["destination_ip"] + ".*"}})

        if kwargs.get("source_port") is not None:
            args.append({"$eq": ["$$t.Source-Port", int(kwargs["source_port"])]})

        if kwargs.get("start_src_port") is not None:
            args.append({"$gte": ["$$t.Source-Port", int(kwargs["start_src_port"])]})

        if kwargs.get("end_src_port") is not None:
            args.append({"$lte": ["$$t.Source-Port", int(kwargs["end_src_port"])]})

        if kwargs.get("destination_port") is not None:
            args.append({"$eq": ["$$t.Destination-Port", int(kwargs["destination_port"])]})

        if kwargs.get("start_dst_port") is not None:
            args.append({"$gte": ["$$t.Destination-Port", int(kwargs["start_dst_port"])]})

        if kwargs.get("end_dst_port") is not None:
            args.append({"$lte": ["$$t.Destination-Port", int(kwargs["end_dst_port"])]})

        if kwargs.get("protocol") is not None:
            kwargs["protocol"] = kwargs["protocol"].upper()
            args.append({"$eq": ["$$t.Protocol", kwargs["protocol"]]})

        if kwargs.get("start_length") is not None:
            args.append({"$gte": ["$$t.Length", int(kwargs["start_length"])]})

        if kwargs.get("end_length") is not None:
            args.append({"$lte": ["$$t.Length", int(kwargs["end_length"])]})

        if kwargs.get("start_ttl") is not None:
            args.append({"$gte": ["$$t.TTL", int(kwargs["start_ttl"])]})

        if kwargs.get("end_ttl") is not None:
            args.append({"$lte": ["$$t.TTL", int(kwargs["end_ttl"])]})

        if len(args) == 0:
            args.append({"$gte": ["$$t.TTL", 0]})

        return args
