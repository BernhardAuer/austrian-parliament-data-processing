import re
from State import State
from InfoItem import InfoItem
from WordType import Wordtype
from Entity import Entity
from HelperFunctions import *

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
    # strip any punctuation
    # word = word.translate(str.maketrans('', '', string.punctuation))
    
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
    
    # detect interjection        
    isInterjection = False
    if word.endswith(":"):        
        word = word.strip(":") 
        isInterjection = True
        
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
    # attention: gedankenstrich
    if word == "–" and "–:" in remainingPhrase: # todo: needs further checks ...
        # edge case: description before speech e.g.:Abg. Leichtfried – in Richtung des das Red­nerpult verlassenden Abg. Scherak –: Also die Rede war jetzt in Ordnung!
        newState = State.BehaviourDescription # todo
        return (newState, remainingPhrase, infoItems)
    
    if word == "–": 
        # edge case: description before speech e.g.:Abg. Leichtfried – in Richtung des das Red­nerpult verlassenden Abg. Scherak –: Also die Rede war jetzt in Ordnung!
        newState = State.NewItem # todo
        return (newState, remainingPhrase, infoItems)
    
    # detect interjection
    isInterjection = False
    if word.endswith(":"):        
        word = word.strip(":") 
        isInterjection = True
    
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
    if isInterjection:
        newState = State.Speech
    else:        
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
    if word.endswith(":"):     
        infoItems[-1].activityList.append("shouting")
        infoItems[-1].quote = "" 
        newState = State.Speech #todo
        return (newState, remainingPhrase, infoItems)
    
    # keep Word as unknown activity
    if not infoItems[-1].activityList:
        infoItems[-1].activityList.append("unknown")
    newState = State.Activity
    return (newState, remainingPhrase, infoItems)

        
def speakerBehaviourDescriptionTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
    if isFillerWord(word):
        return (State.BehaviourDescription, remainingPhrase, infoItems)  
    
    # interjection begins
    if word.endswith(":"):       
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
    
    if infoItems[-1].quote != "":
        infoItems[-1].quote += " "
    infoItems[-1].quote += word    
    # add item to list if not there already
    if "shouting" not in infoItems[-1].activityList:
        infoItems[-1].activityList.append("shouting")
    newState = State.Speech
    return (newState, remainingPhrase, infoItems)

def newItemTransistions(phrase, infoItems):
    word, remainingPhrase = getFirstWord(phrase) 
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
    if word is None: # this is the end
        newState = State.Ending
        return (newState, remainingPhrase, infoItems)
    
    # flag as unknown activity if neccessary #todo check if here neded
    if not infoItems[-1].activityList:
        infoItems[-1].activityList.append("unknown")
    infoItems.append(InfoItem())
    newState = State.Activity
    return (newState, phrase, infoItems)

def addWordToRawSourceText(self, word):
    if self.InfoItem.rawSourceText == "" or re.match("[^\w\s]", word):
        self.InfoItem.rawSourceText += word
    else:
        self.InfoItem.rawSourceText += " " + word
             