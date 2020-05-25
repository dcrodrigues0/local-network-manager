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

    def saveTrafficByHour(self, hourTraffic):
        result = self.updateHour(hourTraffic)

        if result == None:
            self.saveTrafficHourDay(hourTraffic)

        else:
            quantidade = int(result["quantidade_pacotes"]) + int(hourTraffic["quantidade_pacotes"])
            result["quantidade_pacotes"] = quantidade
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
            ips = self.add_new_ips(database_ips, packets)
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

    def add_new_ips(self, ips, packets):

        for ip_address, quantity_packets in packets["Source-IPs"].copy().items():
            if ip_address not in ips["Source-IPs"].keys():
                ips["Source-IPs"][ip_address] = quantity_packets
                del (packets["Source-IPs"][ip_address])

        for ip_address, quantity_packets in ips["Source-IPs"].items():
            if ip_address in packets["Source-IPs"]:
                ips["Source-IPs"][ip_address] += packets["Source-IPs"][ip_address]

        for ip_address, quantity_packets in packets["Destination-IPs"].copy().items():
            if ip_address not in ips["Destination-IPs"].keys():
                ips["Destination-IPs"][ip_address] = quantity_packets
                del (packets["Destination-IPs"][ip_address])

        for ip_address, quantity_packets in ips["Destination-IPs"].items():
            if ip_address in packets["Destination-IPs"]:
                ips["Destination-IPs"][ip_address] += packets["Destination-IPs"][ip_address]

        return ips
