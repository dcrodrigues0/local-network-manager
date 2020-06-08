from container.services.dbutils import mongo
import container.helper.ip_address as ip
from container.util import util
from collections import defaultdict


class Storage(mongo.MongoDAO):
    def __init__(self):
        mongo.MongoDAO.__init__(self)

    def storageAll(self, **Kwargs):
        # self.storageTrafficFull(Kwargs.get("trafficFull"))
        self.saveIntraday(Kwargs.get("trafficIntraday"))
        self.saveTrafficByHour(Kwargs.get("hourTraffic"), Kwargs.get("ip_source_values"))
        self.saveRealTime(Kwargs.get("realTimeTraffic"))
        self.saveTrafficByMac(Kwargs.get("trafficMac"))
        self.saveTrafficByIpAddr(Kwargs.get("trafficIpAddress"))
        self.saveRealTimeTrafficTable(Kwargs.get("realTimeTable"))

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

    def saveTrafficByHour(self, hourTraffic, ips_destiny):
        ip_max_length = self.getSrcIpMaxLength(ips_destiny)
        hourTraffic["ips"] = [ip_max_length]

        result = self.updateHour(hourTraffic)
        if result is None:
            self.saveTrafficHourDay(hourTraffic)

        else:
            has_sum = False

            quantidade = int(result["quantidade_pacotes"]) + int(hourTraffic["quantidade_pacotes"])
            result["quantidade_pacotes"] = quantidade

            for i in range(0, len(result["ips"])):
                if result["ips"][i]["ip"] == hourTraffic["ips"][0]["ip"]:
                    result["ips"][i]["size"] += int(hourTraffic["ips"][0]["size"])
                    has_sum = True

            if has_sum is False:
                print(type(result["ips"]))
                result["ips"].append(hourTraffic["ips"][0])

            self.updateHourMongo(result)

    def saveRealTime(self, realTime):
        self.saveRealTimeTraffic(realTime)

    def saveTrafficByMac(self, trafficMac):
        update = self.updateTrafficByMac(trafficMac)

        if update == None:
            self.saveTrafficMac(trafficMac)
        else:
            quantidade = int(update["quantidade_pacotes"]) + int(trafficMac["quantidade_pacotes"])
            update["quantidade_pacotes"] = quantidade
            self.updateMacMongo(update)

    def saveTrafficByIpAddr(self, packets):
        database_ips = self.getTrafficIps(packets)

        if database_ips is None:
            self.saveTrafficIpAddress(packets)

        else:
            ips = ip.add_new_ips(database_ips, packets)
            self.updateTrafficByIpAddr(ips["_id"], ips)

    def saveRealTimeTrafficTable(self, trafficTable):
        self.saveRealTimeTable(trafficTable)

    def updateIntraday(self, json):
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

    def updateTrafficByMac(self, json):
        result = self.getTrafficMac(json["date"])
        for resp in result:
            return resp
        return None

    def getTrafficIps(self, json):
        result = self.getTrafficIpAddress(json["date"], json["hour"])
        for resp in result:
            return resp
        return None

    def getSrcIpMaxLength(self, jsonIps):

        c = defaultdict(int)
        for d in jsonIps:
            if d["length"] != None:
                c[d['ip']] += int(d['length'])
        value = max(c.items(), key=lambda k: k[1])
        return {"ip": value[0], "size": value[1]}
