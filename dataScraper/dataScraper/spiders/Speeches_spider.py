import scrapy
from dataScraper.Parser.InitStateMachine import initStateMachine
from dataScraper.items import GeneralInfoItem, ParsedInfoItem, SpeechItem, SpeechInfoItem, ApplauseItem, InputCleaner
from scrapy.loader import ItemLoader
import re
import pymongo
import traceback
import logging

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
        self.infoItemParser = initStateMachine()
    
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
        for item in collection.find({'speechUrl': { "$exists": True }, 'speech': { "$exists": False }}):
            url = self.baseUrl + item["speechUrl"]
            urls.append(url)
        client.close()
        return urls
    
    def cleanInput(self, value):
        sanitizedInput = ItemLoader(item=InputCleaner())
        sanitizedInput.add_value('data', value)
        item = sanitizedInput.load_item() 
        
        return item.get("data", "")
    
    def convertEntityListToDictList(self, list):
        dictList = []
        for entity in list:
            dictList.append(entity.asDict())
        return dictList
    
    def parseInfoObject(self, value, paragraph, parentItemLoader, validPersonNames):
        value = self.cleanInput(value)
        results = self.infoItemParser.run(value, validPersonNames)
        
        for parsedItem in results:
            l = ItemLoader(item=ParsedInfoItem(), selector=paragraph)
            l.add_value('activityList', parsedItem.activityList)
            l.add_value('entityList', self.convertEntityListToDictList(parsedItem.entityList))
            l.add_value('quote', parsedItem.quote)
            l.add_value('description', parsedItem.description)
            l.add_value('rawSourceText', parsedItem.rawSourceText) 
            parsedInfoItem = l.load_item()      
            if parsedInfoItem: # filter empty items from buggy parser ...
                parentItemLoader.add_value('parsedInfoItems', dict(parsedInfoItem))

    def getOriginalRequestUrl(self, response, itemLoader):
        url = response.url
        url = url.replace(self.baseUrl, '')
        itemLoader.add_value('requestUrl', url)
        return itemLoader

    def parsePoliticalRole(self, value):
        if "präsidentin des rechnungshofes" in value.lower() or "präsident des rechnungshofes" in value.lower():
            return "presidentOfCourtOfAuditors"
        
        if "präsident" in value.lower(): # Präsident xyz or Präsidentin zx
            return "presidentOfParliament"
        
        if "abgeordnete" in value.lower(): # Abgeordnete xyz or Abgeordneter zy
            return "mp" # member of parliament
        
        return None

    def parse(self, response):
        
        if response.status == 404:
            return None
          
        try:
            currentSpeaker = None
            pureSpeech = None
            currentSpeakerPoliticalRole = None
            isOriginalParlamentaryRequestFollowing = False
            isParlamentaryRequestOngoing = False
            index = 0
            for paragraph in response.css("p"):                
                paragraphAsText = "".join(paragraph.css("*::text").getall())  # todo: check if parsing results are better with or without whitespace
                paragraphAsText = self.cleanInput(paragraphAsText)

                potentialSpeaker = paragraph.css("b a *::text").get() # first entry should be the speaker...
                extractSpeakerRegex = re.search("^[^:]*:", paragraphAsText)

                if potentialSpeaker is not None:
                    potentialSpeaker = self.cleanInput(potentialSpeaker)
                    currentSpeaker = potentialSpeaker
                    if (extractSpeakerRegex is not None):
                        fullNameWithTitles = paragraphAsText[:extractSpeakerRegex.end() - 1] # -1 because of the ":" at the end of the string ...
                        splitNameList = fullNameWithTitles.split(potentialSpeaker)
                        titlesBeforeName = splitNameList[0]
                        if (len(splitNameList) > 1):
                            titlesAfterName = fullNameWithTitles.split(potentialSpeaker)[1]
                        self.logger.debug('title1: %s', titlesBeforeName)
                        self.logger.debug('title2: %s', titlesAfterName)
                        pureSpeech = paragraphAsText[extractSpeakerRegex.end():]
                        currentSpeakerPoliticalRole = self.parsePoliticalRole(titlesBeforeName)
                    else:
                        pureSpeech = paragraphAsText
                else:
                    pureSpeech = paragraphAsText
                timeRegex = re.search("^(\d{1,2}.\d{2}).?\d{0,2}$", paragraphAsText)
                if timeRegex:                    
                    l = ItemLoader(item=SpeechItem(), response=response, selector=paragraph)
                    l.add_value('type', "info")
                    l.add_value('subType', "time")
                    l.add_value('orderId', index)
                    l.add_value('data', timeRegex.group(1)) 
                    l = self.getOriginalRequestUrl(response, l)
                    yield l.load_item()
                    index += 1
                    continue
                
                if "Gesamtwortlaut:".lower() in paragraphAsText.lower():
                    isOriginalParlamentaryRequestFollowing = True
                    
                parlamentaryRequestHeaderList = []
                for header in paragraph.css(".ZM ::text").getall():
                    cleanedHeader = self.cleanInput(header).lower()
                    parlamentaryRequestHeaderList.append(cleanedHeader)
                                    
                if isParlamentaryRequestOngoing or parlamentaryRequestHeaderList:
                    isParlamentaryRequestOngoing = True
                    if isOriginalParlamentaryRequestFollowing:
                        l = ItemLoader(item=SpeechItem(), response=response, selector=paragraph)
                        l.add_value('type', "info")
                        l.add_value('subType', "parlamentaryRequest")
                        l.add_value('orderId', index)
                        l.add_value('data', paragraphAsText) 
                        l = self.getOriginalRequestUrl(response, l)
                        yield l.load_item()
                        index += 1
                    else:
                        l = ItemLoader(item=SpeechItem(), response=response, selector=paragraph)               
                        l.add_value('data', pureSpeech)                                
                        l.add_value('type', "speech")
                        l.add_value('subType', "parlamentaryRequest")
                        l.add_value('orderId', index) 
                        if currentSpeaker is not None:
                            l.add_value('speaker', currentSpeaker) 
                            l.add_value('politicalRole', currentSpeakerPoliticalRole) 
                        l = self.getOriginalRequestUrl(response, l)                                  
                        yield l.load_item()
                        index += 1
                    if "*****" in parlamentaryRequestHeaderList:
                        isParlamentaryRequestOngoing = False
                    continue   
                
                result = re.split(r"[()]", pureSpeech)
                for j, item in enumerate(result):   
                    if item is None or item.strip() == "":
                        continue       
                    if j % 2:       
                        l = ItemLoader(item=GeneralInfoItem(), response=response, selector=paragraph)
                        boldElements = paragraph.css("b")
                        validPersonNames = [self.cleanInput(' '.join(element.css('::text').getall())) for element in boldElements]
                        self.parseInfoObject(item, paragraph, l, validPersonNames)
                        l.add_value('data', item) # this is original data for "info" objects.                          
                        l.add_value('type', "info")
                        l.add_value('orderId', index)
                    else:
                        l = ItemLoader(item=SpeechItem(), response=response, selector=paragraph)               
                        l.add_value('data', item) # this is original data for "info" objects.                                
                        l.add_value('type', "speech")
                        l.add_value('orderId', index) 
                        if currentSpeaker is not None:
                            l.add_value('speaker', currentSpeaker) 
                            l.add_value('politicalRole', currentSpeakerPoliticalRole) 
                             
                    
                    l = self.getOriginalRequestUrl(response, l)                                  
                    yield l.load_item()                    
                    index += 1  
        except Exception as e:
            self.logger.error('an error occured while parsing data:')
            self.logger.error('%s', e)
            self.logger.error('%s', traceback.format_exc())
                
        # yield scrapy.Request(url, self.parse)
        