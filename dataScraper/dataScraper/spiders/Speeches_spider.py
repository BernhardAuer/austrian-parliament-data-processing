import scrapy
import json
from pathlib import Path
from items import SpeechItem, SpeechInfoItem, ApplauseItem, InputCleaner
from scrapy.loader import ItemLoader
from jmespath import search
from datetime import datetime
import re

class SpeechesSpider(scrapy.Spider):
    name = "speeches"
    start_urls = ['https://www.parlament.gv.at/dokument/XXVII/NRSITZ/1/A_-_13_05_25_00208778.html']
    
    handle_httpstatus_list = [404]
    # todo: maybe log / store date of web request?
    
    def cleanInput(self, value):
        sanitizedInput = ItemLoader(item=InputCleaner())
        sanitizedInput.add_value('data', value)
        item = sanitizedInput.load_item() 
        
        return item["data"]
    
    def parseInfoObject(self, value, paragraph):
        value = self.cleanInput(value)
        applauseRegex = re.search("Allgemeiner Beifall.", value)
        if applauseRegex:
            l = ItemLoader(item=ApplauseItem(), selector=paragraph)
            l.add_value('applauseByEntireParties', ["ÖVP", "SPÖ", "FPÖ", "GRÜNE", "NEOS"])
            l.add_value('data', value)
            return l
        applauseRegex = re.search("Beifall bei (?:der )?(.*).", value) # specific applause, needs further matching
        if applauseRegex:
            result = re.split(", | und | sowie bei Abgeordneten von | sowie bei Abgeordneten der | und bei Abgeordneten der ", applauseRegex.group(1))
            l = ItemLoader(item=ApplauseItem(), selector=paragraph)
            l.add_value('applauseByEntireParties', result)
            l.add_value('data', value)
            return l
        l = ItemLoader(item=SpeechInfoItem(), selector=paragraph)
        l.add_value('data', value)
        return l

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
                        l = self.parseInfoObject(item, paragraph)
                        # l.add_value('data', item) # this is original data for "info" objects.                          
                        # l.add_value('type', "info")
                        # l.add_value('orderId', index)
                        # l.add_value('applause', item)
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
        