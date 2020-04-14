from pymongo import MongoClient

class Connection:
    def __init__(self):
        self__client = MongoClient('localhost', 27017)

        print("Server mongo-db version: "+ self__client.server_info()["version"])
