from container.services.dbutils import mongo
from container.util import util
class Service(mongo.MongoDAO):
    def __init__(self):
        mongo.MongoDAO.__init__(self)
        #organiza a conexão


    def getTrafficByDate(self,date):
         return self.makeDataGraph(self.getTrafficByDay(date), 'date', 'avg')

    def getTrafficHourByDate(self, date):
        return self.makeDataGraph(self.getTrafficHour(date), 'hour', 'quantidade_pacotes')

    def getRealTimeService(self):
        return self.makeDataGraph(self.getRealTime(),"min","quantidade_pacotes")

    def getTrafficByMac(self, date):
        return self.makeDataGraph(self.getTrafficMac(date), 'mac_origem', 'quantidade_pacotes')

    def makeDataGraph(self, value, campoLabel, campoDataset):
        labels = []
        dataset = []

        for doc in value:
            labels.append(doc[campoLabel])
            dataset.append(doc[campoDataset])
        #Salve leo rs
        return {'labels': labels, 'datasets': [{ 'data': dataset, 'label':'Quantidade de Pacotes','backgroundColor':'lightblue'}] }

    def getIpTrafficSrc(self, date, hour):
        return self.makeDataIpGraph(self.getTrafficIpAddrSrc(date, hour))

    def makeDataIpGraph(self, value):
        ips = value
        ips_dict = ips.next()
        labels = []
        dataset = []

        for ip, packets in ips_dict['Source-IPs'].items():
            labels.append(util.replace_ip_string(ip, False))
            dataset.append(packets)

        return {'labels': labels, 'datasets': [{ 'data': dataset, 'label':'Quantidade de Pacotes','backgroundColor':'lightblue'}] }
