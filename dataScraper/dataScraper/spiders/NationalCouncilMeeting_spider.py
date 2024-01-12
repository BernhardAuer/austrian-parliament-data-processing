from pathlib import Path
import scrapy
import json
from dataScraper.items import NationalCouncilMeetingItem
from scrapy.loader import ItemLoader


class NationalCouncilMeetingSpider(scrapy.Spider):
    name = "nationalCouncilMeetings"
    search_url = "https://www.parlament.gv.at/Filter/api/json/post?jsMode=EVAL&FBEZ=WFP_007&listeId=11070&showAll=true&export=true"
    
    def __init__(self, gp):
        self.body = {"MODUS": ["PLENAR"], "NRBRBV": ["NR"], "GP": [], "R_SISTEI": ["SI"]}
        self.body["GP"].append(gp)
        
    def start_requests(self):
        return [
            scrapy.Request(
                self.search_url, body=json.dumps(self.body), method="POST", headers={'Content-Type':'application/json'}, callback=self.parsePostData
            )
        ]

    def parsePostData(self, response):
        results = json.loads(response.body)

        for meeting in results["rows"]:
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
