# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dateutil.parser import parse
from itemloaders.processors import MapCompose, Compose, TakeFirst, Join
from dataScraper.validTitlesList import validTitles
from dataScraper.austrianParliamentSpecificTitlesList import austrianParliamentTitles
from jmespath import search
import string
from slugify import slugify
from functools import partial

def parseDate(dateString):
     dateTime = parse(dateString).replace(microsecond=0) # this replace shitty thing is needed for mongodb (js dates only, huh)
     return dateTime

def stripString(value):
     return value.strip()

class NationalCouncilMeetingItem(scrapy.Item):
     name = scrapy.Field(input_processor = MapCompose(stripString), output_processor = TakeFirst()) # 199. Sitzung
     date = scrapy.Field(input_processor = MapCompose(parseDate), output_processor = TakeFirst()) # 20230201
     legislativePeriod  = scrapy.Field(output_processor = TakeFirst()) # XXVII
     meetingType = scrapy.Field(output_processor = TakeFirst()) # NRSTIZ or ...
     meetingNumber = scrapy.Field(input_processor = MapCompose(int), output_processor = TakeFirst()) # 00199
     meetingDay = scrapy.Field(input_processor = MapCompose(int), output_processor = TakeFirst()) # 1
     link = scrapy.Field(output_processor = TakeFirst()) 
     pass


def parseHasSpeechedFinishProperty(value):
     if value == 'fertig':
          return True
     return False

def parseIsVoluntaryTimeLimitProperty(value):
     if value == '*':
          return True
     return False

def convertTimeStringToIntInSec(value):
     # value: (m)m:ss
     (minutes, seconds) = value.split(":")
     totalSeconds = int(seconds) + (int(minutes) * 60)
     return totalSeconds

def convertTimeLimitInMinToSec(value):
     # value: (m)m # tbh this should already be int, but to be sure cast it anyway
     totalSeconds = int(value) * 60
     return totalSeconds

def mergeMeetingDateWithSpeechTime(value, loader_context):
     # value: hh:mm (time in 24h format)
     meetingDate = loader_context.get('meetingDate')
     meetingDate = parse(meetingDate[0])
     (hour, minute) = value.split(":")
     speechDatetime = meetingDate.replace(hour=int(hour), minute=int(minute))
     return speechDatetime

def mergeMeetingDateWithSpeechTimeSeconds(value, loader_context):
     if value is None:
          return None
     # value: hh:mm:ss (time in 24h format)
     meetingDate = loader_context.get('meetingDate')
     meetingDate = parse(meetingDate[0])
     (hour, minute, second) = value.split(":")
     speechDatetime = meetingDate.replace(hour=int(hour), minute=int(minute), second=int(second))
     return speechDatetime

def getTitlesAndPureName(value):
     politicalFunction = []
     for pf in austrianParliamentTitles:
          if pf + ' ' in value:
               politicalFunction.append(pf)
               value = value.replace(pf, '')
     
     parsedTitles = []
     for title in validTitles: # list order is important, eg. because of Mag. and Mag. (FH)
          if title + ' ' in value or value.endswith(title): # whitespace or end of line...
               parsedTitles.append(title)
               value = value.replace(title, '')
     return (politicalFunction, parsedTitles, value)

def getName(value):
     (politicalFunction, parsedTitles, name) = getTitlesAndPureName(value)
     return name

def extractTitles(value):
     (politicalFunction, parsedTitles, name) = getTitlesAndPureName(value)
     return parsedTitles

def extractPoliticalFunction(value):
     (politicalFunction, parsedTitles, name) = getTitlesAndPureName(value)
     return politicalFunction

def matchAndParseDataFromProtocol(value, loader_context):
     if not loader_context.get('hasSpeechFinished'):
          return None
     speechesInProtocol = loader_context.get('speechesInProtocol')
     nrOfSpeechByThisPerson = loader_context.get('nrOfSpeechByThisPerson')
     url = search('[*][?contains(texta, \''+ value +'\')][]', speechesInProtocol)[nrOfSpeechByThisPerson]

     return url

def giveMeError(value, loader_context):
     speechesInProtocol = loader_context.get('speechesInProtocol')
     nrOfSpeechByThisPerson = loader_context.get('nrOfSpeechByThisPerson')

     return speechesInProtocol

def parseVideoUrl(value, loader_context):
     try:
          if not loader_context.get('hasSpeechFinished'):
               return None
          speechData = matchAndParseDataFromProtocol(value, loader_context)
          videoUrl = search('video', speechData)
     except:
          print('parsing error')
          return [None]
     return videoUrl 

def parseSpeechUrl(value, loader_context):
     try:          
          if not loader_context.get('hasSpeechFinished'):
               return None
          speechData = matchAndParseDataFromProtocol(value, loader_context)
          url = search('filename', speechData)     
     except:
          print('parsing error')
          return [None]
     return url 

def parseSpeechTimeFromProtocol(value, loader_context):
     try:          
          if not loader_context.get('hasSpeechFinished'):
               return None
          speechData = matchAndParseDataFromProtocol(value, loader_context)
          time = search('time', speechData)
     except:
          print('parsing error')
          return [None]
     return time

def slugifyConsiderGermanUmlaute(txt):
     return slugify(txt,replacements=[['ü', 'ue'], ['ä', 'ae'], ['ö', 'oe'], ['Ü', 'UE'], ['Ä', 'AE'], ['Ö', 'OE']])

class SpeechesMetaDataItem(scrapy.Item):
     titleBeforeName = scrapy.Field(input_processor = MapCompose(extractTitles, stripString)) # todo: "parlaments"titel wie BM usw.
     nameOfSpeaker = scrapy.Field(input_processor = MapCompose(getName, stripString), output_processor = TakeFirst())
     nameOfSpeakerUrlSlug = scrapy.Field(input_processor = MapCompose(getName, stripString, slugifyConsiderGermanUmlaute), output_processor = TakeFirst())
     titlePrecedingName = scrapy.Field(input_processor = MapCompose(extractTitles, stripString))
     politicalFunction = scrapy.Field(input_processor = MapCompose(extractPoliticalFunction, stripString), output_processor = TakeFirst())
     politicalPartie = scrapy.Field(output_processor = TakeFirst())
     nrOfSpeechByThisPerson = scrapy.Field(output_processor = TakeFirst()) #personSpeechCountInDebate
     typeOfSpeech = scrapy.Field(output_processor = TakeFirst())
     startDateTime = scrapy.Field(input_processor= MapCompose(mergeMeetingDateWithSpeechTime),output_processor = TakeFirst())
     timeLimitInSec = scrapy.Field(input_processor= MapCompose(convertTimeLimitInMinToSec), output_processor = TakeFirst())
     isVoluntaryTimeLimit = scrapy.Field(input_processor= MapCompose(parseIsVoluntaryTimeLimitProperty), output_processor = TakeFirst())
     lengthOfSpeechInSec = scrapy.Field(input_processor= MapCompose(convertTimeStringToIntInSec), output_processor = TakeFirst())
     hasSpeechFinished = scrapy.Field(input_processor= MapCompose(parseHasSpeechedFinishProperty), output_processor = TakeFirst())
     nationalCouncilMeetingTitle = scrapy.Field(output_processor = TakeFirst()) ## ?? really? better use int
     topic = scrapy.Field(output_processor = TakeFirst())
     topicUrlSlug = scrapy.Field(input_processor = MapCompose(slugifyConsiderGermanUmlaute), output_processor = TakeFirst())
     speechNrInDebate = scrapy.Field(output_processor = TakeFirst())
     externalPersonId = scrapy.Field(output_processor = TakeFirst())
     parsingDatetime = scrapy.Field(output_processor = TakeFirst())
     meetingNr = scrapy.Field(output_processor = TakeFirst())
     legislature = scrapy.Field(output_processor = TakeFirst())
     meetingType = scrapy.Field(output_processor = TakeFirst())
     lastEditBySource = scrapy.Field(input_processor = MapCompose(parseDate), output_processor = TakeFirst())
     meetingDate = scrapy.Field(output_processor = TakeFirst())
     topNr = scrapy.Field(output_processor = TakeFirst())
     typeOfDebate = scrapy.Field(output_processor = TakeFirst())
     videoUrl = scrapy.Field(input_processor = MapCompose(getName, stripString, parseVideoUrl), output_processor = TakeFirst())
     speechUrl= scrapy.Field(input_processor = MapCompose(getName, stripString, parseSpeechUrl), output_processor = TakeFirst())
     speechTimeProtocol = scrapy.Field(input_processor = MapCompose(getName, stripString, parseSpeechTimeFromProtocol, mergeMeetingDateWithSpeechTimeSeconds), output_processor = TakeFirst())
     pass

def stripNewline(value):
     return value.replace("\r\n", " ") # strip() does not work for: "randomWord\r\n", only for: "randomWord \r\n"

def stripDuplicateSpaces(value):
     return value.replace("  ", " ")

def stripPunctuation(word):
     return word.strip(string.punctuation)
    
class SpeechItem(scrapy.Item):
     orderId = scrapy.Field(output_processor = TakeFirst())     
     type = scrapy.Field(input_processor = MapCompose(stripString), output_processor = Join())
     subType = scrapy.Field(input_processor = MapCompose(stripString), output_processor = TakeFirst())     
     data = scrapy.Field(input_processor = Compose(MapCompose(stripString, stripNewline), Join(), stripDuplicateSpaces), output_processor = TakeFirst())
     speaker = scrapy.Field(input_processor = MapCompose(getName, stripString, stripPunctuation), output_processor = TakeFirst())
     politicalRole = scrapy.Field(input_processor = MapCompose(stripString), output_processor = TakeFirst())
     requestUrl = scrapy.Field(output_processor = TakeFirst()) 
     pass

class SpeechInfoItem(scrapy.Item):
     orderId = scrapy.Field(output_processor = TakeFirst()) 
     type = scrapy.Field(input_processor = MapCompose(stripString), output_processor = TakeFirst())
     data = scrapy.Field(input_processor = Compose(MapCompose(stripString, stripNewline), Join(), stripDuplicateSpaces), output_processor = TakeFirst())
     requestUrl = scrapy.Field(output_processor = TakeFirst()) 
     pass

class ApplauseItem(scrapy.Item):
     applauseByEntireParties = scrapy.Field()
     applauseByPartsOfParties = scrapy.Field()
     # applauseByPerson = scrapy.Field()
     orderId = scrapy.Field(output_processor = TakeFirst()) 
     type = scrapy.Field(input_processor = MapCompose(stripString), output_processor = TakeFirst())
     data = scrapy.Field(input_processor = Compose(MapCompose(stripString, stripNewline), Join(), stripDuplicateSpaces), output_processor = TakeFirst())
     requestUrl = scrapy.Field(output_processor = TakeFirst()) 
     pass


class ParsedInfoItem(scrapy.Item):
     activityList = scrapy.Field()
     entityList = scrapy.Field()
     description = scrapy.Field(output_processor = TakeFirst()) 
     quote = scrapy.Field(output_processor = TakeFirst()) 
     rawSourceText = scrapy.Field(output_processor = TakeFirst()) 
     pass

class GeneralInfoItem(scrapy.Item):
     parsedInfoItems = scrapy.Field()
     orderId = scrapy.Field(output_processor = TakeFirst()) 
     type = scrapy.Field(input_processor = MapCompose(stripString), output_processor = TakeFirst())
     data = scrapy.Field(input_processor = Compose(MapCompose(stripString, stripNewline), Join(), stripDuplicateSpaces), output_processor = TakeFirst())
     requestUrl = scrapy.Field(output_processor = TakeFirst())
     pass

def replaceHtmlSpecificEscapeChars(value):
     value = value.replace(u'\xa0', u' ') # non-breaking space
     return value.replace('\u00ad','') # soft-hyphen 

class InputCleaner(scrapy.Item):
     data = scrapy.Field(input_processor = Compose(MapCompose(stripString, stripNewline, replaceHtmlSpecificEscapeChars), Join(), stripDuplicateSpaces), output_processor = TakeFirst())
     pass