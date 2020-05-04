from pymongo import MongoClient

class Connection():
    def __init__(self):
        self.__client = MongoClient('mongodb://root:MongoDB!@localhost:27017/')
        self._database = self.__client["network"]

        print("Server mongo-db version: "+ self.__client.server_info()["version"])


    def getDB(self):
        return self._database
