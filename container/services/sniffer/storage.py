from container.services.dbutils import mongo


class Storage(mongo.MongoDAO):
    def __init__(self):
        mongo.MongoDAO.__init__(self)

    def storageAll(self, **Kwargs):
        # self.storageTrafficFull(Kwargs.get("trafficFull"))
        self.saveIntraday(Kwargs.get("trafficIntraday"))
        self.saveTrafficByHour(Kwargs.get("hourTraffic"))
        self.saveRealTime(Kwargs.get("realTimeTraffic"))
        self.saveTrafficByMac(Kwargs.get("trafficMac"))
        self.saveTrafficByIpAddr(Kwargs.get("trafficIpSource"))

    def saveIntraday(self, trafficDay):
        self.saveTrafficDay(trafficDay)

    def saveTrafficByHour(self, hourTraffic):
        self.saveTrafficHourDay(hourTraffic)

    def saveRealTime(self, realTime):
        self.saveRealTimeTraffic(realTime)

    def saveTrafficByMac(self, trafficMac):
        self.saveTrafficMac(trafficMac)

    def saveTrafficByIpAddr(self, packets):
        self.saveTrafficIpSrc(packets)
