from container.services.dbutils import mongo
from container.util import util
class Service(mongo.MongoDAO):
    def __init__(self):
        mongo.MongoDAO.__init__(self)
        #organiza a conexão


    def getTrafficByDate(self,date):
         return util.toJson(self.getTrafficByDay(date))

