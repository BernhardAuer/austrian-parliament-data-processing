import re
from State import State
from InfoItem import InfoItem
from WordType import Wordtype
from Entity import Entity
from HelperFunctions import *

def initialize(phrase, infoItems):
    # initiallize everything
    infoItems = [InfoItem()]
    return (State.DetermineWordMeaning, phrase, infoItems)

def determineWordMeaning(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    
    # -------------------------------------- general tasks ---------------------------------
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
                
    if word == "–": # attention: this is a gedankenstrich (U+2013), not a bindestrich (U+002d)
        return (State.NewItem, remainingPhrase, infoItems)
    
    # skip fillerwords
    if isFillerWord(word):
        return (State.DetermineWordMeaning, remainingPhrase, infoItems)
        
    
    # -------------------------------------- specialized tasks ---------------------------------
    if getActivity(word):
        return (State.Activity, phrase, infoItems)     
    
    if isWordOfType(Wordtype.PRECEDING_Entity_WORDS, stripPunctuation(word)):
        return (State.EntityPersonOrPeople, phrase, infoItems)
        
    if detectPoliticalPartyAbr(word):
        return (State.EntityPoliticalParty, phrase, infoItems) 
    
    # flag as unknown activity if neccessary # todo convert list to set
    if not infoItems[-1].activityList and "unknown" not in infoItems[-1].activityList:
        infoItems[-1].activityList.append("unknown")
    print("unknown word .... precede with parsing")
    return (State.DetermineWordMeaning, remainingPhrase, infoItems) 

def activity(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase)  
    word = stripPunctuation(word)
    
    if isWordOfType(Wordtype.CONNECTING_WORDS, word):
        return (State.Activity, remainingPhrase, infoItems)
        
    # python 3.8 walrus operator -> func return val gets added to list only if not null
    if activity := getActivity(word):
        infoItems[-1].activityList.append(activity)
        if "unknown" in infoItems[-1].activityList:
            infoItems[-1].activityList.remove("unknown")
        return (State.Activity, remainingPhrase, infoItems)
    
    return (State.DetermineWordMeaning, phrase, infoItems) 

def entity_PoliticalParty(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase)         
    isInterjectionFollowing = word.endswith(":")    
    word = stripPunctuation(word)
    
    if isFillerWord(word) or isWordOfType(Wordtype.CONNECTING_WORDS, word):
        return (State.EntityPoliticalParty, remainingPhrase, infoItems)
    
    if entity := detectPoliticalPartyAbr(word):
        entityInstance = Entity("politicalParty", entity)
        infoItems[-1].entityList.append(entityInstance) 

    if isInterjectionFollowing:       
        return (State.Interjection, remainingPhrase, infoItems)
    elif entity:
        return (State.EntityPoliticalParty, remainingPhrase, infoItems) 
    
    return (State.DetermineWordMeaning, phrase, infoItems)   

def entity_PersonOrPeople(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase)
    isInterjectionFollowing = word.endswith(":") 
    isEndOfCurrentEntity = word.endswith(".") # todo: this is a temp fix (right now we don't know when a person name ends....)
    word = stripPunctuation(word)    
    
    if isFillerWord(word) or isWordOfType(Wordtype.CONNECTING_WORDS, word) or isWordOfType(Wordtype.PRECEDING_Entity_WORDS, stripPunctuation(word)):
        return (State.EntityPersonOrPeople, remainingPhrase, infoItems)
    
    # detect descriptive behaviour of speaker
    # attention: gedankenstrich
    if word == "–" and "–:" in remainingPhrase: # todo: needs further checks ...
        # edge case: description before speech e.g.:Abg. Leichtfried – in Richtung des das Red­nerpult verlassenden Abg. Scherak –: Also die Rede war jetzt in Ordnung!
        return (State.BehaviourDescription, remainingPhrase, infoItems)
    
    entity = detectPoliticalPartyAbr(word)    
    if entity:
        # some persons of a political party
        entityInstance = Entity("somePersonsOfPoliticalParty", entity)
        infoItems[-1].entityList.append(entityInstance)
    else:
        # name of specific person  
        entityInstance = Entity("person", word) # todo: this needs further enhancements for full names ....
        infoItems[-1].entityList.append(entityInstance) 
         
    if isInterjectionFollowing:
        return (State.Interjection, remainingPhrase, infoItems)
    elif not isEndOfCurrentEntity: # todo: this is a temp fix ...
        return (State.EntityPersonOrPeople, remainingPhrase, infoItems)
    
    return (State.DetermineWordMeaning, remainingPhrase, infoItems)
        
def behaviourDescription(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    if word.endswith("–:"):
        return (State.Interjection, remainingPhrase, infoItems)
    
    if infoItems[-1].description != "":
        infoItems[-1].description += " "
    infoItems[-1].description += word
    return (State.BehaviourDescription, remainingPhrase, infoItems)

def interjection(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase)
    if word == "" or word == "–":
        return (State.DetermineWordMeaning, remainingPhrase, infoItems)
    
    if infoItems[-1].quote != "":
        infoItems[-1].quote += " "
    infoItems[-1].quote += word
    
    # add item to list if not there already
    if "shouting" not in infoItems[-1].activityList:
        infoItems[-1].activityList.append("shouting")
        if "unknown" in infoItems[-1].activityList:
            infoItems[-1].activityList.remove("unknown")
    return (State.Interjection, remainingPhrase, infoItems)

def newItem(phrase, infoItems):
    infoItems.append(InfoItem())
    return (State.DetermineWordMeaning, phrase, infoItems)

def addWordToRawSourceText(self, word):
    if self.InfoItem.rawSourceText == "" or re.match("[^\w\s]", word):
        self.InfoItem.rawSourceText += word
    else:
        self.InfoItem.rawSourceText += " " + word
             