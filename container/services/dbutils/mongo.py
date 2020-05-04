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


    def saveTrafficDay(self, json):
        print("Start Insert day network traffic")
        self._db.trafficIntraday.insert(json)
        print("Finish Insert day network traffic")

    def saveTrafficHourDay(self, json):
        print("Start Insert hour by day network traffic")
        self._db.trafficHour.insert(json)
        print("Finish Insert hour by day network traffic")

    # --------- GET --------
    def getTrafficByDay(self, date):
        return self._db.trafficIntraday.find( {"date":date})
