from dataScraper.spiders.NationalCouncilMeeting_spider import NationalCouncilMeetingSpider
from dataScraper.spiders.SpeechesMetaData_spider import SpeechesMetaDataSpider
from dataScraper.spiders.Speeches_spider import SpeechesSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
import logging
from scrapy.utils.log import configure_logging
from datetime import datetime

# https://victorsanner.nl/azure/scraping/container/instances/docker/2022/04/25/cheap-and-easy-scraping-using-scrapy-docker-and-azure-container-instances.html

MODE_INCREMENTAL = "incremental"
MODE_OVERWRITE = "overwrite"


def configureLogging():
    configure_logging(install_root_handler=False)
    # see https://stackoverflow.com/a/64617052 
    # this is also interesting https://stackoverflow.com/a/52930823
    configure_logging(settings={
        "LOG_STDOUT": True
    })
    formattedDate = datetime.now().strftime("%Y-%m-%d")
    logfileName = "./logs/scrapy_" + formattedDate + ".log"
    file_handler = logging.FileHandler(logfileName, mode="a")
    formatter = logging.Formatter(
        fmt="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel("INFO")
    logging.root.addHandler(file_handler)    

def scrape():
    configureLogging()
    settings = get_project_settings()
    
    mongodbUri = None
    mode = settings["MODE"]
    try:
        mongodbUri = os.environ['MONGODB_URI']
        logging.info(f'read env variable MONGODB_URI: "{mongodbUri}"')
    except:
        logging.info('could not read env variable MONGODB_URI')
        
    try:
        mode = os.environ['MODE']
        logging.info(f'read env variable MODE: "{mode}"')
    except:
        logging.info('could not read env variable MODE')

    if not mongodbUri:
        customSettings = settings            
    else:
        overridenSettings = {
            "MONGODB_URI": mongodbUri
        }
        customSettings = settings._to_dict() | overridenSettings 
         
    customSettings = settings    
    gps = [
          'XX',
          'XXI',
          'XXII',
          'XXIII',
          'XXIV',
          'XXV',
          'XXVI',
          'XXVII',
          ]
    process = CrawlerProcess(customSettings)
    logging.info(f"loaded custom app settings. mongoDbUri: '{customSettings['MONGODB_URI']}', mode: '{mode}', gps: {gps}")
    if mode == MODE_OVERWRITE:
        logging.info(f"queue crawlers in data overwrite mode")  
        for gp in gps:
            logging.info(f"queue NationalCouncilMeetingSpider for GP '{gp}'")             
            process.crawl(NationalCouncilMeetingSpider, gp)
        for gp in gps:
            logging.info(f"queue SpeechesMetaDataSpider for GP '{gp}'")  
            process.crawl(SpeechesMetaDataSpider, gp)
        logging.info(f"queue SpeechesSpider") 
        process.crawl(SpeechesSpider)
    elif mode == MODE_INCREMENTAL:
        logging.info(f"queue crawlers in incremental data update mode")  
        currentGp = gps[-1]
        logging.info(f"queue NationalCouncilMeetingSpider for GP '{currentGp}'") 
        process.crawl(NationalCouncilMeetingSpider, currentGp)
        logging.info(f"queue SpeechesMetaDataSpider for GP '{currentGp}'")  
        process.crawl(SpeechesMetaDataSpider, currentGp)
        logging.info(f"queue SpeechesSpider") 
        process.crawl(SpeechesSpider)
    
    logging.info(f"start scrape process")  
    process.start() # the script will block here until the crawling is finished
    logging.info(f"finished scrape process")  

scrape()