import scrapy
import json
from pathlib import Path
from items import SpeechItem, SpeechInfoItem, ApplauseItem, InputCleaner
from scrapy.loader import ItemLoader
from jmespath import search
from datetime import datetime
import re
import pymongo

class SpeechesSpider(scrapy.Spider):
    name = "speeches"
    start_urls = []
    
    handle_httpstatus_list = [404]
    # todo: maybe log / store date of web request?
    
    custom_settings = {
        'ITEM_PIPELINES': {
            'dataScraper.pipelines.InsertToSpeechCollectionPipeline': 400
        }
    }
    
    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri = mongodb_uri
        self.mongodb_db = mongodb_db
        if not self.mongodb_uri: sys.exit("You need to provide a Connection String.")
        self.baseUrl = 'https://www.parlament.gv.at'
        self.start_urls = self.get_urls_from_db()
    
    @classmethod
    def from_crawler(cls, crawler):    

        spider = cls(
            mongodb_uri=crawler.settings.get('MONGODB_URI'),
            mongodb_db=crawler.settings.get('MONGODB_DATABASE')
        )
        spider._set_crawler(crawler)
        return spider  

    def get_urls_from_db(self):
        client = pymongo.MongoClient(self.mongodb_uri)
        db = client[self.mongodb_db]        
        collection = db["speechesMetaData"]
        urls = []
        for item in collection.find({'speechUrl': { "$exists": True }}).limit(30):
            url = self.baseUrl + item["speechUrl"]
            urls.append(url)
        client.close()
        return urls
    
    def cleanInput(self, value):
        sanitizedInput = ItemLoader(item=InputCleaner())
        sanitizedInput.add_value('data', value)
        item = sanitizedInput.load_item() 
        
        return item.get("data", "")
    
    def parseInfoObject(self, value, paragraph):
        value = self.cleanInput(value)
        applauseRegex = re.search("Allgemeiner Beifall.", value)
        if applauseRegex:
            l = ItemLoader(item=ApplauseItem(), selector=paragraph)
            l.add_value('applauseByEntireParties', ["ÖVP", "SPÖ", "FPÖ", "GRÜNE", "NEOS"])
            l.add_value('data', value)
            l.add_value('type', "info")     
            return l
        applauseRegex = re.search("Beifall bei (?:der )?(.*).", value) # specific applause, needs further matching
        if applauseRegex:            
            partialApplause = re.split(" sowie bei Abgeordneten von | sowie bei Abgeordneten der | und bei Abgeordneten der | bei Abgeordneten von | bei Abgeordneten der ", applauseRegex.group(1))
            l = ItemLoader(item=ApplauseItem(), selector=paragraph)
            if len(partialApplause) > 1:
                # this means that partial applause by at least one party/parlamentarian happened
                partialApplauseByParties = re.split(", | und ", partialApplause[1])   
                l.add_value('applauseByPartsOfParties', partialApplauseByParties)                                 
            applauseByEntireParties = re.split(", | und ", partialApplause[0])
                        
            l.add_value('applauseByEntireParties', applauseByEntireParties)
            l.add_value('data', value)
            l.add_value('type', "info") 
            return l
        # applause not parsable ...
        l = ItemLoader(item=SpeechInfoItem(), selector=paragraph)
        if "Beifall" in value:
            print("error while parsing unknown applause")
            l.add_value('type', "unknown applause")    
        
        l.add_value('type', "info")    
        l.add_value('data', value)
        return l

    def getOriginalRequestUrl(self, response, itemLoader):
        url = response.url
        url = url.replace(self.baseUrl, '')
        itemLoader.add_value('requestUrl', url)
        return itemLoader

    def parse(self, response):
        
        if response.status == 404:
            return None
          
        try:
            currentSpeaker = None
            pureSpeech = None
            index = 0
            for paragraph in response.css("p"):
                potentialSpeaker = paragraph.css("b a *::text").get() # first entry should be the speaker...
                
                paragraphAsText = "".join(paragraph.css("*::text").getall())  # todo: check if parsing results are better with or without whitespace
                paragraphAsText = self.cleanInput(paragraphAsText)              
                extractSpeakerRegex = re.search("^(Abgeordneter|Präsident)*\s*([^:]*)\s*(\(.+\))*:", paragraphAsText)  
                print(paragraphAsText)              
                if potentialSpeaker is not None:
                    currentSpeaker = potentialSpeaker
                    if (extractSpeakerRegex is not None):
                        pureSpeech = paragraphAsText[extractSpeakerRegex.end():]
                    else:
                        pureSpeech = paragraphAsText
                else:
                    pureSpeech = paragraphAsText
                
                timeRegex = re.search("^\d{1,2}.\d{2}$", paragraphAsText)
                if timeRegex:                    
                    l = ItemLoader(item=SpeechItem(), response=response, selector=paragraph)
                    l.add_value('type', "info")
                    l.add_value('orderId', index)
                    l.add_value('data', paragraphAsText) 
                    l = self.getOriginalRequestUrl(response, l)
                    yield l.load_item()
                    index += 1
                    continue
                
                result = re.split(r"[()]", pureSpeech)
                for j, item in enumerate(result):   
                    if item is None or item.strip() == "":
                        continue                
                    
                    if j % 2:                         
                        l = self.parseInfoObject(item, paragraph)
                        # l.add_value('data', item) # this is original data for "info" objects.                          
                        # l.add_value('type', "info")
                        l.add_value('orderId', index)
                        # l.add_value('applause', item)
                    else:
                        l = ItemLoader(item=SpeechItem(), response=response, selector=paragraph)               
                        l.add_value('data', item) # this is original data for "info" objects.                                
                        l.add_value('type', "speech")
                        l.add_value('orderId', index) 
                        if currentSpeaker is not None:
                            l.add_value('speaker', currentSpeaker)  
                    
                    l = self.getOriginalRequestUrl(response, l)                                  
                    yield l.load_item()                    
                    index += 1  
        except Exception as e:
            print("an error occured while parsing data:")
            print(e) 
                
        # yield scrapy.Request(url, self.parse)
        