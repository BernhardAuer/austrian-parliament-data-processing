from pathlib import Path
import scrapy
import json
from dataScraper.mongoProvider import MongoProvider
from dataScraper.items import NationalCouncilMeetingItem
from scrapy.loader import ItemLoader


class NationalCouncilMeetingSpider(scrapy.Spider):
    name = "nationalCouncilMeetings"
    search_url = "https://www.parlament.gv.at/Filter/api/json/post?jsMode=EVAL&FBEZ=WFP_007&listeId=11070&showAll=true&export=true"
    
    def __init__(self, gp, mongodb_uri, mongodb_db):
        self.body = {"MODUS": ["PLENAR"], "NRBRBV": ["NR"], "GP": [gp], "R_SISTEI": ["SI"]}
        mongo_provider = MongoProvider(
            mongodb_uri,
            mongodb_db,
            self.name
        )        
        collection = mongo_provider.get_collection()
        latestItem = list(collection.find({"legislativePeriod": gp}).sort("meetingNumber", -1).limit(1))
        self.nextMeetingNr = latestItem[0]["meetingNumber"] + 1 if len(latestItem) else 1
        self.logger.info(f"start national council meeting scraping with meetingNr {self.nextMeetingNr} of gp: {gp}")
        
    @classmethod
    def from_crawler(cls, crawler, gp):
        spider = cls(
            gp,
            mongodb_uri=crawler.settings.get('MONGODB_URI'),
            mongodb_db=crawler.settings.get('MONGODB_DATABASE')
        )
        spider._set_crawler(crawler)
        return spider 
           
    def start_requests(self):
        return [
            scrapy.Request(
                self.search_url, body=json.dumps(self.body), method="POST", headers={'Content-Type':'application/json'}, callback=self.parsePostData
            )
        ]

    def parsePostData(self, response):
        self.logger.debug(f"requestUrl: '{response.request.url}'")
        results = json.loads(response.body)

        for meeting in results["rows"]:
            if int(meeting[5]) < self.nextMeetingNr:
                continue 
            
            # todo: maybe use jmespath?
            l = ItemLoader(item=NationalCouncilMeetingItem(), selector=meeting)
            l.add_value("name", meeting[1])
            l.add_value("date", meeting[7])
            l.add_value("legislativePeriod", meeting[3])
            l.add_value("meetingType", meeting[4])
            l.add_value("meetingNumber", meeting[5])
            l.add_value("meetingDay", meeting[9])
            l.add_value("link", meeting[10])

            yield l.load_item()
