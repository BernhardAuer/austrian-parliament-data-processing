import pymongo

class MongoProvider(object):

    def __init__(self, uri, database, collection):
        self.mongoUri = uri
        self.mongoDb = database
        self.collection = collection

    def get_collection(self):
        self.client = pymongo.MongoClient(self.mongoUri)
        return self.client[self.mongoDb][self.collection]

    def close_connection(self):
        self.client.close()