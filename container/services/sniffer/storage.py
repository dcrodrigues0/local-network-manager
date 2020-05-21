from container.services.dbutils import mongo
from container.util import util
class Storage(mongo.MongoDAO):
    def __init__(self):
        mongo.MongoDAO.__init__(self)

    def storageAll(self, **Kwargs):
        # self.storageTrafficFull(Kwargs.get("trafficFull"))
        self.saveIntraday(Kwargs.get("trafficIntraday"))
        self.saveTrafficByHour(Kwargs.get("hourTraffic"))
        self.saveRealTime(Kwargs.get("realTimeTraffic"))
        self.saveTrafficByMac(Kwargs.get("trafficMac"))
        self.saveTrafficByIpAddr(Kwargs.get("trafficIpAddress"))

    def saveIntraday(self, trafficDay):
        update = self.updateIntraday(trafficDay)

        if update == None:
            json = trafficDay
            self.saveTrafficDay(json)

        else:
            quantidade = int(trafficDay["quantidade_pacotes"]) + int(update["quantidade_pacotes"])
            tamanho = int(trafficDay["tamanho_pacotes"]) + int(update["tamanho_pacotes"])

            json = {'date': trafficDay["date"], 'tamanho_pacotes': tamanho, 'quantidade_pacotes': quantidade,
                'avg': util.formatFloat(tamanho / quantidade)}
            self.updateIntradayMongo(update["_id"], json)

    def saveTrafficByHour(self, hourTraffic):
        result = self.updateHour(hourTraffic)

        if result == None:
            self.saveTrafficHourDay(hourTraffic)

        else:
            print("Update hour")
            quantidade = int(result["quantidade_pacotes"]) + int(hourTraffic["quantidade_pacotes"])
            result["quantidade_pacotes"] = quantidade
            print(result)
            self.updateHourMongo(result)

    def saveRealTime(self, realTime):
        self.saveRealTimeTraffic(realTime)

    def saveTrafficByMac(self, trafficMac):
        self.saveTrafficMac(trafficMac)

    def saveTrafficByIpAddr(self, packets):
        self.saveTrafficIpAddress(packets)


    def updateIntraday(self,json):
        result = self.getTrafficByDay(json["date"])
        for resp in result:
            return resp
        return None

    def updateHour(self, json):
        result = self.getTrafficHour(json["date"])
        for resp in result:
            if resp["hour"] == json["hour"]:
                return resp
        return None
