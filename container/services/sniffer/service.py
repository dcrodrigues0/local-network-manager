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

    def makeDataGraph(self, value, campoLabel, campoDataset):
        labels = []
        dataset = []

        for doc in value:
            labels.append(doc[campoLabel])
            dataset.append(doc[campoDataset])
        #Salve leo rs
        return {'labels': labels, 'datasets': [{ 'data': dataset, 'label':'Quantidade de Pacotes','backgroundColor':'lightblue'}] }

