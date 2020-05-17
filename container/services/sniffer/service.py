from container.services.dbutils import mongo
from container.util import util



class Service(mongo.MongoDAO):
    def __init__(self):
        mongo.MongoDAO.__init__(self)
        # organiza a conexão

    def getTrafficByDate(self, date):
        return self.makeDataGraph(self.getTrafficByDay(date), 'date', 'avg')

    def getTrafficHourByDate(self, date):
        return self.makeDataGraph(self.getTrafficHour(date), 'hour', 'quantidade_pacotes')

    def getRealTimeService(self):
        return self.makeDataGraph(self.getRealTime(), "min", "quantidade_pacotes")

    def getTrafficByMac(self, date):
        return self.makeDataGraph(self.getTrafficMac(date), 'mac_origem', 'quantidade_pacotes')

    def getTrafficByRange(self, start, end):

        start = start.split("-")
        end = end.split("-")

        contentField = self.getTrafficBetween()
        traffic = []

        for content in contentField:
            if content["date"].split("-")[1] >= start[1] and content["date"].split("-")[1] <= end[1]:
                if content["date"].split("-")[0] >= start[0] and content["date"].split("-")[0] <= end[0]:
                    traffic.append(content)

        return self.makeDataGraph(traffic, 'date', 'quantidade_pacotes')

    def makeDataGraph(self, value, campoLabel, campoDataset):
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
                'datasets': [{'data': dataset, 'label': 'Quantidade de Pacotes', 'backgroundColor': colors}]}

    def getTrafficIp(self, date, hour, direction):
        return self.makeDataIpGraph(self.getTrafficIpAddress(date, hour), direction)


    def makeDataIpGraph(self, value, direction):
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
                'datasets': [{'data': dataset, 'label': 'Quantidade de Pacotes', 'backgroundColor': colors}]}
