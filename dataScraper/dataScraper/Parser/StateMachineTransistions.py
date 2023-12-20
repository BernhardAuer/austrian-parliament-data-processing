import re
from State import State
from InfoItem import InfoItem
from WordType import Wordtype
from Entity import Entity
from HelperFunctions import *

def startTransitions(phrase, infoItems):
    # initiallize everything
    infoItems = [InfoItem()]
    return (State.DetermineWordMeaning, phrase, infoItems)

def determineWordMeaningTransitions(phrase, infoItems):
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
        newState = State.Activity
        return (newState, phrase, infoItems)     
    
    wordWithoutPunctuation = word.translate(str.maketrans('', '', string.punctuation))
    if isWordOfType(Wordtype.PRECEDING_Entity_WORDS, wordWithoutPunctuation):                    
        newState = State.BeginningOfEntity
        return (newState, phrase, infoItems)
        
    if detectPoliticalPartyAbr(word):            
        newState = State.EntityPoliticalParty
        return (newState, phrase, infoItems) 


def activityTransitions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase)          
    activity = getActivity(word)
    infoItems[-1].activityList.append(activity)
    return (State.ActivityConnectingWord, remainingPhrase, infoItems) 

def activityConnectingWordTransistions( phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase)
    if isWordOfType(Wordtype.CONNECTING_WORDS, word):
        return (State.Activity, remainingPhrase, infoItems) 
    
    return (State.DetermineWordMeaning, phrase, infoItems)  

def detectBeginningOfEntityTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase)
    word = word.strip(".")  
    # strip any punctuation todo
    # word = word.translate(str.maketrans('', '', string.punctuation))
     
    if isWordOfType(Wordtype.PRECEDING_Entity_WORDS, word): 
        return (State.EntityPersonOrPeople, remainingPhrase, infoItems) 
     
    return (State.DetermineWordMeaning, phrase, infoItems)

def entityPoliticalPartyTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 

    endsWithComma = False
    if word.endswith(","):
        word = word.strip(",")
        endsWithComma = True        

    # detect interjection        
    isInterjection = False
    if word.endswith(":"):        
        word = word.strip(":") 
        isInterjection = True
    
    if isFillerWord(word):
        return (State.EntityPoliticalParty, remainingPhrase, infoItems)
    
    # check if re-transition is needed ...
    if isWordOfType(Wordtype.PRECEDING_Entity_WORDS, word):
        return (State.DetermineWordMeaning, phrase, infoItems)  
      
    entity = detectPoliticalPartyAbr(word)    
    # no known entity detected
    if entity is None:
        return (State.DetermineWordMeaning, phrase, infoItems) 
    
    entityInstance = Entity("politicalParty", entity)
    infoItems[-1].entityList.append(entityInstance) 
    if endsWithComma:        
        newState = State.EntityPoliticalParty
    elif isInterjection:       
        newState = State.Speech
    else:
        newState = State.EntityPoliticalPartyConnectingWord
    return (newState, remainingPhrase, infoItems) 

def entityPersonOrPeopleTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase)
    
    endsWithComma = False
    if word.endswith(","):
        word = word.strip(",")
        endsWithComma = True        
    
    endsWithPeriod = False
    if word.endswith("."):
        word = word.strip(".")
        endsWithPeriod = True        
    
    # detect interjection
    isInterjection = False
    if word.endswith(":"):        
        word = word.strip(":") 
        isInterjection = True
        
    if isFillerWord(word):
        return (State.EntityPersonOrPeople, remainingPhrase, infoItems)
    
    # detect descriptive behaviour of speaker
    # attention: gedankenstrich
    if word == "–" and "–:" in remainingPhrase: # todo: needs further checks ...
        # edge case: description before speech e.g.:Abg. Leichtfried – in Richtung des das Red­nerpult verlassenden Abg. Scherak –: Also die Rede war jetzt in Ordnung!
        newState = State.BehaviourDescription # todo
        return (newState, remainingPhrase, infoItems)
    
    # detect connecting word
    if isWordOfType(Wordtype.CONNECTING_WORDS, word):
        newState = State.EntityPersonOrPeopleConnectingWord # todo
        return (newState, remainingPhrase, infoItems)
    
    entity = detectPoliticalPartyAbr(word)    
    # some persons of specific party
    if entity is not None:    
        entityInstance = Entity("somePersonsOfPoliticalParty", entity)
        infoItems[-1].entityList.append(entityInstance)
    
    # specific person (full name)   
    entityInstance = Entity("person", word) # todo: this needs further enhancements for full names ....
    infoItems[-1].entityList.append(entityInstance) 
    
    if endsWithComma:
        newState = State.EntityPersonOrPeopleConnectingWord # todo
        return (newState, remainingPhrase, infoItems)
    
    if endsWithPeriod:
        newState = State.DetermineWordMeaning
        return (newState, remainingPhrase, infoItems)
     
    if isInterjection:
        newState = State.Speech
    else:        
        newState = State.EntityPersonOrPeople
    return (newState, remainingPhrase, infoItems)  

def entityPoliticalPartyConnectingWordTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    if isWordOfType(Wordtype.CONNECTING_WORDS, word):
        newState = State.BeginningOfEntity
        return (newState, remainingPhrase, infoItems) 
    
    return (State.DetermineWordMeaning, phrase, infoItems) 

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
        
def speakerBehaviourDescriptionTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    # interjection begins
    if word.endswith("–:"):       
        newState = State.Speech
        return (newState, remainingPhrase, infoItems)
    infoItems[-1].description += " " + word # todo: whitespace on beginning....
    newState = State.BehaviourDescription
    return (newState, remainingPhrase, infoItems)

def speechTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase)
    if word == "" or word == "–":
        return (State.DetermineWordMeaning, remainingPhrase, infoItems)
    
    if infoItems[-1].quote != "":
        infoItems[-1].quote += " "
    infoItems[-1].quote += word
    
    # add item to list if not there already
    if "shouting" not in infoItems[-1].activityList:
        infoItems[-1].activityList.append("shouting")
    return (State.Speech, remainingPhrase, infoItems)

def newItemTransistions(phrase, infoItems):
    # flag as unknown activity if neccessary #todo check if here neded
    if not infoItems[-1].activityList:
        infoItems[-1].activityList.append("unknown")
    infoItems.append(InfoItem())
    newState = State.DetermineWordMeaning
    return (newState, phrase, infoItems)

def addWordToRawSourceText(self, word):
    if self.InfoItem.rawSourceText == "" or re.match("[^\w\s]", word):
        self.InfoItem.rawSourceText += word
    else:
        self.InfoItem.rawSourceText += " " + word
             