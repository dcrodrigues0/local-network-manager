from container.services.dbutils import mongo

class Storage(mongo.MongoDAO):
    def __init__(self):
        mongo.MongoDAO.__init__(self)
        #organiza a conexão


    def storageAll(self,**Kwargs):
        #self.storageTrafficFull(Kwargs.get("trafficFull"))
        self.saveIntraday(Kwargs.get("trafficIntraday"))
        self.saveTrafficByHour(Kwargs.get("hourTraffic"))
        self.saveTrafficByMac(Kwargs.get("trafficMac"))


    def storageTrafficFull(self, trafficFull):
        self.saveTraffic(trafficFull)


    def saveTraffic(self, data):
        self.saveTrafficFull(data)

    def saveIntraday(self, trafficDay):
        self.saveTrafficDay(trafficDay)

    def saveTrafficByHour(self, hourTraffic):
        self.saveTrafficHourDay(hourTraffic)

    def saveTrafficByMac(self, trafficMac):
        self.saveTrafficMac(trafficMac)
