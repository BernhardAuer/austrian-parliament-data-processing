import scrapy
import json
from dataScraper.items import SpeechesMetaDataItem
from scrapy.loader import ItemLoader
from jmespath import search
from datetime import datetime
import traceback
from dataScraper.mongoProvider import MongoProvider

class SpeechesMetaDataSpider(scrapy.Spider):
    name = "speechesMetaData"
    meetingNr = 1
    urlPlaceholder = ''
    start_urls = []
    
    handle_httpstatus_list = [404]
    # todo: maybe log / store date of web request?
    
    def __init__(self, gp, mongodb_uri, mongodb_db):
        mongo_provider = MongoProvider(
            mongodb_uri,
            mongodb_db,
            self.name
        )
        
        collection = mongo_provider.get_collection()
        latestItem = list(collection.find().sort("meetingNr", -1).limit(1))
        self.meetingNr = latestItem[0]["meetingNr"] + 1 if len(latestItem) else 1
        self.urlPlaceholder = 'https://www.parlament.gv.at/gegenstand/%s/NRSITZ/' % gp + '%d?json=true'
        self.start_urls = [self.urlPlaceholder % self.meetingNr]
        
    @classmethod
    def from_crawler(cls, crawler, gp):    

        spider = cls(
            gp,
            mongodb_uri=crawler.settings.get('MONGODB_URI'),
            mongodb_db=crawler.settings.get('MONGODB_DATABASE')
        )
        spider._set_crawler(crawler)
        return spider 
     
    def parse(self, response):
        
        if response.status == 404:
            return None
            
        try:
            jsonAsPythonObject = json.loads(response.body)
            
            meetingDate = search('content[].info.sessiondate', jsonAsPythonObject)
            meetingNr = search('content[].inr', jsonAsPythonObject)
            legislature = search('content[].gp_code', jsonAsPythonObject)
            meetingType = search('content[].ityp', jsonAsPythonObject) # NRSITZ or ...
            lastEditBySource = search('content[].update', jsonAsPythonObject)
            nationalCouncilMeetingTitle = search('content[].info.title', jsonAsPythonObject)
            debates = search('content[].past_debates[]', jsonAsPythonObject)
            typetextDict = {}
            
            for singleDebate in debates:

                topic = search('text', singleDebate)
                topNr = search('top', singleDebate)
                typeOfDebate = search('type', singleDebate)
                speechesInProtocol = None
                if topNr is not None:
                    speechesInProtocol = search('content[].progress[?starts_with(text, \'' + topNr + ' \' )].speeches[]', jsonAsPythonObject) 
                else:              
                    typetext = search('typetext', singleDebate)
                    if typetext in typetextDict:
                        typetextDict[typetext] += 1
                    else:
                        typetextDict[typetext] = 0
                        
                    
                    progressObjectList = search('content[].progress[]', jsonAsPythonObject)
                    
                    mergedProgressObjectDict = {}
                    # group by
                    for progressObject in progressObjectList:                       
                        key = progressObject['text']
                        speeches = search('speeches[]', progressObject)

                        if key not in mergedProgressObjectDict:
                            mergedProgressObjectDict[key] = [speeches]
                        else:
                            mergedProgressObjectDict[key].append(speeches)  
                    
                    currentDebatteTitleList = search('keys(@)[?contains(@, \'' + typetext + ' \' )]', mergedProgressObjectDict)
                    currentDebatteTitle = ""
                    if 0 <= typetextDict[typetext] < len(currentDebatteTitleList): # check if index exists
                        currentDebatteTitle = currentDebatteTitleList[typetextDict[typetext]]
                        speechesInProtocol = list(mergedProgressObjectDict[currentDebatteTitle])
                    

                speeches = search('speeches', singleDebate)
                nameDict = {}
                for singleSpeech in speeches:
                    hasSpeechFinished = singleSpeech[1] == 'fertig'
                    if singleSpeech[2] not in nameDict:
                        nameDict[singleSpeech[2]] = 0
                       
                    isVoluntaryTimeLimit = singleSpeech[9] if singleSpeech[9] != None else 'unfreiwillig lol' # quick fix, there must be a better solution for null values

                    l = ItemLoader(item=SpeechesMetaDataItem(), meetingDate = meetingDate, speechesInProtocol = speechesInProtocol, nrOfSpeechByThisPerson = nameDict[singleSpeech[2]], hasSpeechFinished = hasSpeechFinished, selector=singleSpeech)      

                    l.add_value('titleBeforeName', singleSpeech[2],    re='^([^,]*),?.*\(.+\)$') # needs extra parsing ...
                    l.add_value('nameOfSpeaker', singleSpeech[2],      re='^([^,]*),?.*\(.+\)$') # needs extra parsing ...
                    l.add_value('politicalFunction', singleSpeech[2],  re='^([^,]*),?.*\(.+\)$') # needs extra parsing ...
                    l.add_value('titlePrecedingName', singleSpeech[2], re='^[^,]*,?(.*)\(.+\)$')  
                    l.add_value('politicalPartie', singleSpeech[2], re='\((\S+)\)$')
                    l.add_value('typeOfSpeech', singleSpeech[5])
                    l.add_value('startDateTime', singleSpeech[6])
                    l.add_value('lengthOfSpeechInSec', singleSpeech[7])
                    l.add_value('isVoluntaryTimeLimit', isVoluntaryTimeLimit)
                    l.add_value('timeLimitInSec', singleSpeech[8])
                    l.add_value('hasSpeechFinished', singleSpeech[1])
                    l.add_value('legislature', legislature)
                    l.add_value('meetingType', meetingType)
                    l.add_value('meetingNr', meetingNr)
                    l.add_value('nationalCouncilMeetingTitle', nationalCouncilMeetingTitle)
                    l.add_value('topic', topic)
                    l.add_value('topNr', topNr)
                    l.add_value('typeOfDebate', typeOfDebate) 
                    l.add_value('speechNrInDebate', singleSpeech[0]) 
                    l.add_value('nrOfSpeechByThisPerson', nameDict[singleSpeech[2]])
                    l.add_value('externalPersonId', singleSpeech[3]) 
                    l.add_value('lastEditBySource', lastEditBySource)
                    l.add_value('parsingDatetime',  datetime.now()) 
                    l.add_value('videoUrl', singleSpeech[2], re='^([^,]*),?.*\(.+\)$')
                    l.add_value('speechUrl',  singleSpeech[2], re='^([^,]*),?.*\(.+\)$') 
                    l.add_value('speechTimeProtocol',  singleSpeech[2], re='^([^,]*),?.*\(.+\)$') 
                    
                    if hasSpeechFinished and singleSpeech[2] in nameDict:
                        nameDict[singleSpeech[2]] += 1
                            
                    yield l.load_item()
        except Exception as e:
            self.logger.error('an error occured while parsing data:')
            self.logger.error('%s', e)
            self.logger.error('%s', traceback.format_exc())
            
        self.meetingNr += 1
        url = self.urlPlaceholder % self.meetingNr        
        yield scrapy.Request(url, self.parse)

        #example json
        #  "speeches": [
        #                 [
        #                     1,
        #                     "fertig",
        #                     "Mag. Faika El-Nagashi (G)",
        #                     5651,
        #                     0,
        #                     "p",
        #                     "10:27",
        #                     "4:56",
        #                     4,
        #                     "*"
        #                 ],
        #                 [
        #                     2,
        #                     "fertig",
        #                     "Dietmar Keck (S)",
        #                     14840,
        #                     0,
        #                     "p",
        #                     "10:32",
        #                     "3:51",
        #                     3,
        #                     "*"
        #                 ]
        #               ]