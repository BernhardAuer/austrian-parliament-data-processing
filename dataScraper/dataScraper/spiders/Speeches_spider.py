import scrapy
import json
from pathlib import Path
from items import SpeechItem, SpeechInfoItem
from scrapy.loader import ItemLoader
from jmespath import search
from datetime import datetime
import re

class SpeechesSpider(scrapy.Spider):
    name = "speeches"
    start_urls = ['https://www.parlament.gv.at/dokument/XXVII/NRSITZ/1/A_-_13_05_25_00208778.html']
    
    handle_httpstatus_list = [404]
    # todo: maybe log / store date of web request?
    
    def parse(self, response):
        
        if response.status == 404:
            return None
          
        try:
            currentSpeaker = None
            pureSpeech = None
            index = 0
            for paragraph in response.css("p"):
                paragraphAsText = " ".join(paragraph.css("*::text").getall())
                extractSpeakerRegex = re.search("^(Abgeordneter|Präsident)*\s*(.*)\s*(\(.+\))*:", paragraphAsText)
                if (extractSpeakerRegex is not None):
                    currentSpeaker = extractSpeakerRegex.group(2)
                    pureSpeech = paragraphAsText[extractSpeakerRegex.end():]
                else:
                    pureSpeech = paragraphAsText
                
                timeRegex = re.search("^\d{1,2}.\d{2}$", paragraphAsText)
                if timeRegex:                    
                    l = ItemLoader(item=SpeechItem(), response=response, selector=paragraph)
                    l.add_value('type', "info-time")
                    l.add_value('orderId', index)
                    l.add_value('data', paragraphAsText) 
                    yield l.load_item()
                    index += 1
                    continue
                
                result = re.split(r"[()]", pureSpeech)
                for j, item in enumerate(result):   
                    if item == "" or item is None:
                        continue                
                    
                    if j % 2: 
                        l = ItemLoader(item=SpeechInfoItem(), response=response, selector=paragraph)
                        l.add_value('data', item) # this is original data for "info" objects.                          
                        l.add_value('type', "info")
                        l.add_value('orderId', index)
                        l.add_value('applause', item)
                    else:
                        l = ItemLoader(item=SpeechItem(), response=response, selector=paragraph)                           
                        l.add_value('data', item) # this is original data for "info" objects.                                
                        l.add_value('type', "speech")
                        l.add_value('orderId', index) 
                        if currentSpeaker is not None:
                            l.add_value('speaker', currentSpeaker)                                    
                    yield l.load_item()                    
                    index += 1  
        except Exception as e:
            print("an error occured while parsing data:")
            print(e) 
                
        # yield scrapy.Request(url, self.parse)
        