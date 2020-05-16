from container.database import connection as conn


class MongoDAO():
    def __init__(self):
        self._conn = conn.Connection()
        self.initConnection()

    def initConnection(self):
        self._db = self._conn.getDB()

    def saveTrafficFull(self, json):
        print("Start Insert full network traffic")
        self._db.trafficfull.insert_many(json)
        print("Finish Insert full network traffic")

    def saveTrafficMac(self, json):
        print("Start Insert Mac network traffic")
        self._db.trafficMac.insert(json)
        print("Finish Insert Mac network traffic")

    def saveTrafficDay(self, json):
        print("Start Insert day network traffic")
        self._db.trafficIntraday.insert(json)
        print("Finish Insert day network traffic")

    def saveTrafficHourDay(self, json):
        print("Start Insert hour by day network traffic")
        self._db.trafficHour.insert(json)
        print("Finish Insert hour by day network traffic")

    def saveRealTimeTraffic(self, json):
        print("Start Insert realtime traffic")
        self._db.realTime.insert(json)
        print("Finish Insert realtime traffic")

    def saveTrafficIpAddress(self, json):
        print("Start Insert packets by source ip address traffic")
        self._db.trafficIp.insert(json)
        print("Finish Insert packets by source ip address traffic")

    # --------- GET --------

    def getTrafficByDay(self, date):
        return self._db.trafficIntraday.find( {"date":date})

    def getTrafficHour(self, date):
        return self._db.trafficHour.find( {"date":date})

    def getRealTime(self):
        return self._db.realTime.find({})

    def getTrafficMac(self, date):
        return self._db.trafficMac.find( {"date":date})

    def getTrafficIpAddress(self, date, hour):
        return self._db.trafficIp.find({"date": date, "hour": hour})

    def getTrafficBetween(self):
        return self._db.trafficIntraday.find({})

