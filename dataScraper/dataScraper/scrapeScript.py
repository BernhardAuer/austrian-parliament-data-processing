from spiders.NationalCouncilMeeting_spider import NationalCouncilMeetingSpider
from spiders.SpeechesMetaData_spider import SpeechesMetaDataSpider
from spiders.Speeches_spider import SpeechesSpider
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import sys
import os

# https://victorsanner.nl/azure/scraping/container/instances/docker/2022/04/25/cheap-and-easy-scraping-using-scrapy-docker-and-azure-container-instances.html

#this is where we start the scraper 
def scrape():
    settings = get_project_settings()
    
    mongodbUri=""
    try:
        mongodbUri = os.environ['MONGODB_URI']
    except:
        print("could not read env variable mongodb_uri")
    finally:
        if not mongodbUri:
            customSettings = settings            
        else:
            overridenSettings = {
                "MONGODB_URI": mongodbUri
            }
            customSettings = settings._to_dict() | overridenSettings

    customSettings = settings   
    speechesMetaDataBaseUrl = 'https://www.parlament.gv.at/gegenstand/XXVII/NRSITZ/197?json=true'
    gps = ['XXVII',
          'XXVI',
          'XXV',
          'XXIV',
          'XXIII',
          'XXII',
          'XXI',
          'XX',
          ]

    process = CrawlerProcess(customSettings)
    process.crawl(NationalCouncilMeetingSpider)
    for gp in gps:
        process.crawl(SpeechesMetaDataSpider, gp)
    process.crawl(SpeechesSpider)
    process.start() # the script will block here until the crawling is finished

scrape()