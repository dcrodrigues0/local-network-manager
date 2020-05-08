from container.services.dbutils import mongo
from container.util import util
class Service(mongo.MongoDAO):
    def __init__(self):
        mongo.MongoDAO.__init__(self)
        #organiza a conexão


    def getTrafficByDate(self,date):
         return self.makeDataGraph(self.getTrafficByDay(date), 'date', 'avg')


    def getTrafficHourByDate(self, date):
        return self.makeDataGraph(self.getTrafficHour(date), 'hour', 'date')


    def makeDataGraph(self, value, campoLabel, campoDataset):
        labels = []
        dataset = []

        for doc in value:
            labels.append(doc[campoLabel])
            dataset.append(doc[campoDataset])

        return {'labels': labels, 'dataset': { 'data': dataset}}

