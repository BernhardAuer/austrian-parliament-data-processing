import copy
import re
from StateMachine import StateMachine

class Wordtype:
    PRECEDING_Entity_WORDS = "precedingEntityWord"
    CONNECTING_WORDS = "connectingWords"

class State:
    Start = "Start"
    Activity = "DetectActivity"
    ActivityConnectingWord = "ActivityConnectingWord"
    BeginningOfEntity = "BeginningOfEntity"
    EntityPoliticalParty = "DetectEntityName"
    EntityPersonOrPeople = "EntityPersonOrPeople"
    EntityPoliticalPartyConnectingWord = "EntityPoliticalPartyConnectingWord"
    EntityPersonOrPeopleConnectingWord = "EntityPersonOrPeopleConnectingWord"
    BehaviourDescription = "BehaviourDescription"
    Speech = "Speech"
    ImplicitActivity = "DetectActivityImplicit"
    NewItem = "NewItem"     
    Ending = "Ending"     

class Entity:
    def __init__(self, type, name):
        self.type = type # person, politicalParty, somePersonsOfPoliticalParty
        self.name = name    
    def __str__(self):
        return "Entity-type: " + self.type + "; name: " + self.name 
    def asDict(self):
        return {'type': self.type, 'name': self.name}

class InfoItem:
    def __init__(self):
        self.rawSourceText = "" # the orignial string, from which this item is beeing parsed
        self.subType = "" # ?? applause, ...
        self.activityList = [] # list of strings, eg. applause, cheerfulness, ...
        self.entityList = [] # list of Entity() objects
        self.description = "" # further information/description about this parsed activity
        self.quote = "" # quote from the spoken shouts / speech from a person
    
    def __str__(self):
        return ("activityList: " + ",".join(self.activityList) 
        + ";\nentityList: \n" + ",\n".join([str(entityItem) for entityItem in self.entityList]) 
        + ";\nquote: " + self.quote
        + ";\ndescription: " + self.description
        + ";\nrawSourceText: " + self.rawSourceText)
    
# class SpeechInfoParserStateMachine(object):
# def __init__(self, logger):
#     # self.currentState = StateMachineAction.DetectActivity
#     self.activityList = []
#     self.entityList = []
#     self.PersonOrPartsOfPartyAsEntityFollowing = False
#     self.PersonNameSplitByWhitespace = False
#     self.Speech = None
#     self.PersonNameWithDash = False
#     self.InfoItem = InfoItem()
#     self.ResultList = []
#     self.logger = logger

def isWordOfType(type, word):        
    connectingWordsList = ["und", ",", "sowie"]
    precedingEntityWordsList = ["abgeordnete","abg","abgeordneten"]
    match type:
        case Wordtype.CONNECTING_WORDS:
            if word.lower() in connectingWordsList:
                return True    
        case Wordtype.PRECEDING_Entity_WORDS:
            if word.lower() in precedingEntityWordsList:
                return True        
        # case _: 
            # logger.error("unknown type!")            
    return False

def getActivity(word):
    activityDict = {
        "beifall": "applause",
        "zwischenruf": "shouting",
        "zwischenrufe": "shouting",
        "ruf": "shouting",
        "heiterkeit": "cheerfulness"
    }
    return activityDict.get(word.lower()) 
    
def detectPoliticalPartyAbr(word):
    entityDict = {
        "övp": "övp",
        "fpö": "fpö",
        "spö": "spö",
        "grünen": "grüne",
        "grüne": "grüne",
        "neos": "neos"
    }
    return entityDict.get(word.lower()) 

def isFillerWord(word):
    fillerWords = ["bei", "den", "der", "die", "das", "von", "des", "dem"]        
    return word in fillerWords

def getFirstWord(txt):
    splitted_txt = txt.split(" ", 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    return (word, txt)

def startTransitions(txt, infoItems):
    # word, txt = self.getFirstWord(txt)
    newState = State.Activity
    # initiallize everything
    infoItems = [InfoItem()]
    return (newState, txt, infoItems)

def activityTransitions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
    if isFillerWord(word):
        return (State.Activity, remainingPhrase, infoItems)               
    activity = getActivity(word)
    
    # no activity detected
    if activity is None:
        newState = State.BeginningOfEntity
        return (newState, phrase, infoItems)       
    
    # additional activity todo: ??? for what is this shit again? cant remember ...
    # new activity / new entity
    # if self.InfoItem.activityList and self.InfoItem.entityList: 
    #     newState = State.Ending
    #     return (newState, remainingPhrase, infoItems)
    
    infoItems[-1].activityList.append(activity)                    
    newState = State.ActivityConnectingWord
    return (newState, remainingPhrase, infoItems) 

def activityConnectingWordTransistions( phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase)
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
    if isFillerWord(word):
        return (State.ActivityConnectingWord, remainingPhrase, infoItems)  
    isConnectingWord = isWordOfType(Wordtype.CONNECTING_WORDS, word)
    
    # new activity
    if isConnectingWord:
        newState = State.Activity
        return (newState, remainingPhrase, infoItems) 
    
    newState = State.BeginningOfEntity
    return (newState, phrase, infoItems)  

def detectBeginningOfEntityTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
        
    word = word.strip(".")  
    
    if isFillerWord(word):
        return (State.BeginningOfEntity, remainingPhrase, infoItems)  
    isEntityFollowing = isWordOfType(Wordtype.PRECEDING_Entity_WORDS, word)
    if isEntityFollowing:                    
        newState = State.EntityPersonOrPeople
        return (newState, remainingPhrase, infoItems)  
    return (State.EntityPoliticalParty, phrase, infoItems)

def entityPoliticalPartyTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
    
    endsWithComma = False
    if word.endswith(","):
        word = word.strip(",")
        endsWithComma = True        
        
    if isFillerWord(word):
        return (State.EntityPoliticalParty, remainingPhrase, infoItems)
    
    # check if re-transition is needed ...
    isEntityFollowing = isWordOfType(Wordtype.PRECEDING_Entity_WORDS, word)
    if isEntityFollowing:                    
        newState = State.BeginningOfEntity
        return (newState, phrase, infoItems)  
      
    entity = detectPoliticalPartyAbr(word)
    
    # no known entity detected
    if entity is None:            
        newState = State.ImplicitActivity # todo check this ...
        return (newState, phrase, infoItems) 
    
    entityInstance = Entity("politicalParty", entity)
    infoItems[-1].entityList.append(entityInstance) 
    if endsWithComma:        
        newState = State.EntityPoliticalParty
    else:        
        newState = State.EntityPoliticalPartyConnectingWord
    return (newState, remainingPhrase, infoItems) 

def entityPersonOrPeopleTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
    
    endsWithComma = False
    if word.endswith(","):
        word = word.strip(",")
        endsWithComma = True        
    
    word = word.strip(".")  
    
    if isFillerWord(word):
        return (State.EntityPersonOrPeople, remainingPhrase, infoItems)  
    # detect descriptive behaviour of speaker
    if word == "–": # attention: gedankenstrich
        # edge case: description before speech e.g.:Abg. Leichtfried – in Richtung des das Red­nerpult verlassenden Abg. Scherak –: Also die Rede war jetzt in Ordnung!
        newState = State.BehaviourDescription # todo
        return (newState, remainingPhrase, infoItems)
    
    # detect interjection
    if word == ":":
        newState = State.Speech
        return (newState, remainingPhrase, infoItems)
    
    # detect connecting word      
    isConnectingWord = isWordOfType(Wordtype.CONNECTING_WORDS, word)
    if isConnectingWord:
        newState = State.EntityPersonOrPeopleConnectingWord # todo
        return (newState, phrase, infoItems)
    
    # detect "abg."" etc.
    isEntityFillerWord = isWordOfType(Wordtype.PRECEDING_Entity_WORDS, word)
    if isEntityFillerWord:                    
        newState = State.BeginningOfEntity
        return (newState, phrase, infoItems) 
    
    entity = detectPoliticalPartyAbr(word)
    
    # some persons of specific party
    if entity is not None:    
        entityInstance = Entity("somePersonsOfPoliticalParty", entity)
        infoItems[-1].entityList.append(entityInstance)        
        newState = State.EntityPersonOrPeople
        return (newState, remainingPhrase, infoItems)
    
    # specific person (full name)   
    entityInstance = Entity("person", word) # todo: this needs further enhancements for full names ....
    infoItems[-1].entityList.append(entityInstance)          
    newState = State.EntityPersonOrPeople
    return (newState, remainingPhrase, infoItems)  

def entityPoliticalPartyConnectingWordTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase)
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
    if isFillerWord(word):
        return (State.EntityPoliticalPartyConnectingWord, remainingPhrase, infoItems)  
    isConnectingWord = isWordOfType(Wordtype.CONNECTING_WORDS, word)
    
    # new entity
    if isConnectingWord:
        newState = State.BeginningOfEntity
        return (newState, remainingPhrase, infoItems) 
    
    newState = State.BeginningOfEntity
    return (newState, phrase, infoItems) 

def entityPersonOrPeopleConnectingWordTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase)
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
    if isFillerWord(word):
        return (State.EntityPersonOrPeopleConnectingWord, remainingPhrase, infoItems)  
    isConnectingWord = isWordOfType(Wordtype.CONNECTING_WORDS, word)
    
    # new entity
    if isConnectingWord:
        newState = State.EntityPersonOrPeople
        return (newState, remainingPhrase, infoItems) 
    
    newState = State.BeginningOfEntity
    return (newState, phrase, infoItems) 

def implicitActivityTransistions( phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
    if isFillerWord(word):
        return (State.ImplicitActivity, remainingPhrase, infoItems)  
    
    # interjection begins
    if word == ":":     
        infoItems[-1].activityList.append("shouting")
        infoItems[-1].quote = "" 
        newState = State.Speech #todo
        return (newState, remainingPhrase, infoItems)
    newState = State.NewItem
    return (newState, remainingPhrase, infoItems)

        
def speakerBehaviourDescriptionTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
    if isFillerWord(word):
        return (State.BehaviourDescription, remainingPhrase, infoItems)  
    
    # interjection begins
    if word == ":":       
        newState = State.Speech #todo
        return (newState, remainingPhrase, infoItems)
    infoItems[-1].description += " " + word # todo: whitespace on beginning....
    newState = State.BehaviourDescription
    return (newState, remainingPhrase, infoItems)

def speechTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
    if isFillerWord(word):
        return (State.Speech, remainingPhrase, infoItems)  
    if word == "–": # attention: gedankenstrich
        newState = State.NewItem
        return (newState, remainingPhrase, infoItems)
    
    infoItems[-1].quote += " " + word
    newState = State.Speech
    return (newState, remainingPhrase, infoItems)

def newItemTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
    if word is None: # this is the end
        newState = State.Ending
        return (newState, remainingPhrase, infoItems)
    
    infoItems.append(InfoItem())
    newState = State.Activity
    return (newState, phrase, infoItems)


def doParsing(input):
    infoItem = [InfoItem()]
    m = StateMachine()
    m.add_state(State.Start, startTransitions)
    m.add_state(State.Activity, activityTransitions, infoItem)
    m.add_state(State.ActivityConnectingWord, activityConnectingWordTransistions, infoItem)
    m.add_state(State.BeginningOfEntity, detectBeginningOfEntityTransistions, infoItem)
    m.add_state(State.EntityPersonOrPeople, entityPersonOrPeopleTransistions, infoItem)
    m.add_state(State.EntityPoliticalParty, entityPoliticalPartyTransistions, infoItem)
    m.add_state(State.EntityPoliticalPartyConnectingWord, entityPoliticalPartyConnectingWordTransistions, infoItem)
    m.add_state(State.EntityPersonOrPeopleConnectingWord, entityPersonOrPeopleConnectingWordTransistions, infoItem)
    m.add_state(State.BehaviourDescription, speakerBehaviourDescriptionTransistions, infoItem)
    m.add_state(State.ImplicitActivity, implicitActivityTransistions, infoItem)
    m.add_state(State.NewItem, newItemTransistions, infoItem)
    m.add_state(State.Ending, None, infoItem, end_state=1)
    m.set_start(State.Start)
    m.run(input)

          
    # # self.logger.debug("("geparste Aktivität:")
    # # self.logger.debug("(self.activityList)
    # # self.logger.debug("("geparste entitäten:")
    # # self.logger.debug("(self.entityList)
    # # self.logger.debug("("geparste rede:")
    # # self.logger.debug("(self.Speech)
    # # self.logger.debug("("-----------------")
    # for result in self.ResultList:
    #     # self.logger.debug("("\nITEM:")
    #     # self.logger.debug("(result)
def addWordToRawSourceText(self, word):
    if self.InfoItem.rawSourceText == "" or re.match("[^\w\s]", word):
        self.InfoItem.rawSourceText += word
    else:
        self.InfoItem.rawSourceText += " " + word
             
   
       
       
       
# test = SpeechInfoParserStateMachine(None)
# test.doParsing("Beifall und Heiterkeit bei der FPÖ, ÖVP sowie bei Abgeordneten der SPÖ und den Grünen, dem Abg. Brandstätter und der Abgeordneten Cornellia Ecker. – Heiterkeit bei den Grünen und bei Abgeordneten der SPÖ. – Zwischenruf bei der SPÖ.")
# test.doParsing("Beifall bei den Grünen sowie der Abg. Cornelia Julia Ecker.")
# test.doParsing("Beifall bei den Grünen sowie der Abgeordneten Herr und Kucharowits.")
# test.doParsing("Abg. Meinl-Reisinger: Geh bitte, he! Das ist ein bisschen sehr überheblich!")
#test.doParsing("Zwischenrufe der Abgeordneten Heinisch-Hosek und Kucharowits.")
# test.doParsing("Abg. Ottenschläger: Das war jetzt sehr streng! – Beifall bei den Grünen sowie der Abgeordneten Herr und Kucharowits.")
# test.doParsing("Abg. Ottenschläger: Das war jetzt sehr streng! – Weitere Rufe bei der ÖVP: Streng!")
# test.doParsing("in die rechte Ecke zeigend")
# test.doParsing("Allgemeiner Beifall. –  hallo, das ist ein test –  und noch ein test")
# test.doParsing("Abg. Leichtfried – in Richtung des das Rednerpult verlassenden Abg. Scherak –: Also die Rede war jetzt in Ordnung!")
# test.doParsing("Zwischenruf des Abg. Hafenecker. – Abg. Stögmüller – in Richtung Abg. Hafenecker –: Für die Bevölkerung ist die Polizei zuständig, Herr Kollege! – Präsident Sobotka gibt das Glockenzeichen.")

# test.doParsing("Heiterkeit und Beifall bei den Grünen sowie Beifall der Abg. Herr.")





doParsing("Beifall und Heiterkeit bei der FPÖ, ÖVP sowie bei Abgeordneten der SPÖ, Neos und den Grünen, dem Abg. Brandstätter und der Abgeordneten Cornellia Ecker.")
#doParsing("Beifall bei den Grünen sowie der Abg. Cornelia Julia Ecker.")
#doParsing("Beifall bei den Grünen sowie der Abgeordneten Herr und Kucharowits.")