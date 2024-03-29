# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import sys

class MongoDBPipeline:
    
    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri = mongodb_uri
        self.mongodb_db = mongodb_db
        if not self.mongodb_uri: sys.exit("You need to provide a Connection String.")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get('MONGODB_URI'),
            mongodb_db=crawler.settings.get('MONGODB_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongodb_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):    
        data = dict(item)
        self.db[spider.name].insert_one(data)
        return item

class InsertToSpeechCollectionPipeline:
    
    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri = mongodb_uri
        self.mongodb_db = mongodb_db
        if not self.mongodb_uri: sys.exit("You need to provide a Connection String.")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get('MONGODB_URI'),
            mongodb_db=crawler.settings.get('MONGODB_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongodb_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):    
        data = dict(item)
        requestUrl = data.pop('requestUrl')
        self.db["speechesMetaData"].update_one({"speechUrl": requestUrl}, {"$push": {"speech": data}})
        return item