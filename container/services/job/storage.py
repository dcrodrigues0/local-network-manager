class Storage():
    def __init__(self):
        #organiza a conexão
        pass


    def storageAll(self,**Kwargs):
        self.storageTrafficFull(Kwargs.get("trafficFull"))
        self.storageIntraday(Kwargs.get("trafficIntraday"))


    def storageTrafficFull(self, trafficFull):
        for data in trafficFull:
            self.saveTraffic(data)


    def saveTraffic(self, data):
        pass

    def storageIntraday(self, trafficDay):
        print(trafficDay)
