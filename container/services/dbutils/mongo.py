from container.database import connection as conn
import container.log.colorer
import logging


class MongoDAO():
    def __init__(self):
        self._conn = conn.Connection()
        self.initConnection()
        logging.basicConfig(level=logging.DEBUG)

    def initConnection(self):
        self._db = self._conn.getDB()

    def saveTrafficFull(self, json):
        logging.info("Start Insert full network traffic")
        self._db.trafficfull.insert_many(json)
        logging.info("Finish Insert full network traffic")

    def saveTrafficMac(self, json):
        logging.info("Start Insert Mac network traffic")
        self._db.trafficMac.insert(json)
        logging.info("Finish Insert Mac network traffic")

    def saveTrafficDay(self, json):
        logging.info("Start Insert day network traffic")
        self._db.trafficIntraday.insert(json)
        logging.info("Finish Insert day network traffic")

    def saveTrafficHourDay(self, json):
        logging.info("Start Insert hour by day network traffic")
        self._db.trafficHour.insert(json)
        logging.info("Finish Insert hour by day network traffic")

    def saveRealTimeTraffic(self, json):
        logging.info("Start Insert realtime traffic")
        self._db.realTime.insert(json)
        logging.info("Finish Insert realtime traffic")

    def saveTrafficIpAddress(self, json):
        logging.info("Start Insert packets by IP address traffic")
        self._db.trafficIp.insert(json)
        logging.info("Finish Insert packets by IP address traffic")

    def saveRealTimeTable(self, json):
        logging.info("Start Insert traffic real time table")
        self._db.trafficTable.insert(json)
        logging.info("Finish Insert traffic real time table")

    def updateIntradayMongo(self, id, json):
        logging.info("Update intraday")
        self._db.trafficIntraday.update(
            {"_id": id},
            {"$set":
                 {"quantidade_pacotes": json["quantidade_pacotes"],
                  "tamanho_pacotes": json["tamanho_pacotes"],
                  "avg": json["avg"]},
             }, upsert=True)

    def updateHourMongo(self, json):
        logging.info("Update Hour")
        self._db.trafficHour.update(
            {"_id": json['_id']},
            {"$set":
                 {"quantidade_pacotes": json["quantidade_pacotes"]},
             }, upsert=True)

    def updateMacMongo(self, json):
        logging.info("Update Mac")
        self._db.trafficMac.update(
            {"_id": json['_id']},
            {"$set":
                 {"quantidade_pacotes": json["quantidade_pacotes"]},
             }, upsert=True)

    def updateTrafficByIpAddr(self, id, json):
        logging.info("Update IP Addresses")
        self._db.trafficIp.update(
            {"_id": id},
            {"$set":
                 {"Source-IPs": json["Source-IPs"],
                  "Destination-IPs": json["Destination-IPs"]},
             })

    # --------- GET --------

    def getTrafficByDay(self, date):
        return self._db.trafficIntraday.find({"date": date})

    def getTrafficHour(self, date):
        return self._db.trafficHour.find({"date": date})

    def getRealTime(self):
        return self._db.realTime.find({})

    def getTrafficMac(self, date):
        return self._db.trafficMac.find({"date": date})

    def getTrafficIpAddress(self, date, hour):
        return self._db.trafficIp.find({"date": date, "hour": hour})

    def getTrafficBetween(self):
        return self._db.trafficIntraday.find({})

    def getRealTimeTrafficTable(self, filter_args, date_args, limit):
        pipeline = [
            {
                "$project": {
                    "_id": 0,
                    "Traffic": {
                        "$filter": {
                            "input": "$Traffic",
                            "as": "t",
                            "cond": {
                                "$and": filter_args
                            }
                        }
                    }
                }
            },
            {"$unwind": "$Traffic"},
            {"$limit": limit}
        ]

        if date_args is not None:
            pipeline.insert(0, date_args)

        return self._db.trafficTable.aggregate(pipeline)

