import scrapy
import json
from pathlib import Path
from items import SpeechItem
from scrapy.loader import ItemLoader
from jmespath import search
from datetime import datetime
import re

class SpeechesSpider(scrapy.Spider):
    name = "speeches"
    start_urls = ['https://www.parlament.gv.at/dokument/XXVII/NRSITZ/1/A_-_12_56_19_00208775.html']
    
    handle_httpstatus_list = [404]
    # todo: maybe log / store date of web request?
    
    def parse(self, response):
        
        if response.status == 404:
            return None
          
        try:
            for index, paragraph in enumerate(response.css("p.MsoNormal")):            
                l = ItemLoader(item=SpeechItem(), response=response, selector=paragraph)  
                paragraphAsText = " ".join(paragraph.css("*::text").getall())
                print(paragraphAsText)
                extractSpeakerRegex = re.search("^(Abgeordneter|Präsident)*\s*(.*)\s*(\(.+\))*:", paragraphAsText)
                if (extractSpeakerRegex is not None):
                    print("reges:")
                    print(extractSpeakerRegex.group(2)) 
                    l.add_value('speaker', extractSpeakerRegex.group(2))
                    speechOnly = paragraphAsText[extractSpeakerRegex.end():]
                    l.add_value('data', speechOnly)
                # l.add_css('type', "::text")   # important: space before ::text is needed, so that all child elements get parsed
                l.add_value('orderId', index)
                l.add_value('type', "speech")

                yield l.load_item()
        except Exception as e:
            print("an error occured while parsing data:")
            print(e) 
                
        # yield scrapy.Request(url, self.parse)
        