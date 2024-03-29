from dataScraper.Parser.State import State
from dataScraper.Parser.InfoItem import InfoItem
from dataScraper.Parser.WordType import Wordtype
from dataScraper.Parser.Entity import Entity
from dataScraper.Parser.HelperFunctions import *

def unpackPhraseAndInfoItems(kwds):
    return kwds["phrase"], kwds["infoItems"]

def initialize(**kwds):
    # initialize everything
    infoItems = []
    return (State.NewItem, kwds["phrase"], infoItems)

def newItem(**kwds):
    phrase, infoItems = unpackPhraseAndInfoItems(kwds)
    infoItems.append(InfoItem())
    # default: flag as unknown activity
    # todo convert list to set
    infoItems[-1].activityList.append("unknown")
    return (State.DetermineWordMeaning, phrase, infoItems)

def determineWordMeaning(**kwds):
    phrase, infoItems = unpackPhraseAndInfoItems(kwds)
    word, remainingPhrase = getFirstWord(phrase)
    wordWithoutPunctuation = stripPunctuation(word)

    # -------------------------------------- general tasks ---------------------------------
    if word == "":
        return (State.Ending, remainingPhrase, infoItems)
                
    if word == "–": # attention: this is a gedankenstrich (U+2013), not a bindestrich (U+002d)
        return (State.NewItem, remainingPhrase, infoItems)
    
    # skip fillerwords
    if isFillerWord(wordWithoutPunctuation):
        infoItems[-1].addToRawSourceText(word)
        return (State.DetermineWordMeaning, remainingPhrase, infoItems)
        
    
    # -------------------------------------- specialized tasks ---------------------------------
    if getActivity(wordWithoutPunctuation):
        return (State.Activity, phrase, infoItems)     
    
    if isWordOfType(Wordtype.PRECEDING_Entity_WORDS, wordWithoutPunctuation):
        return (State.EntityPersonOrPeople, phrase, infoItems)
        
    if detectPoliticalPartyAbr(wordWithoutPunctuation):
        return (State.EntityPoliticalParty, phrase, infoItems) 

    infoItems[-1].addToRawSourceText(word)
    # print("unknown word .... precede with parsing") # todo: use logger ...
    return (State.DetermineWordMeaning, remainingPhrase, infoItems) 

def activity(**kwds):
    phrase, infoItems = unpackPhraseAndInfoItems(kwds)
    word, remainingPhrase = getFirstWord(phrase)  
    wordWithoutPunctuation = stripPunctuation(word)
    
    if isWordOfType(Wordtype.CONNECTING_WORDS, wordWithoutPunctuation):
        infoItems[-1].addToRawSourceText(word)
        return (State.Activity, remainingPhrase, infoItems)
    
    if word.endswith(":"):
        infoItems[-1].addToRawSourceText(word)
        return (State.Interjection, remainingPhrase, infoItems)
    
    # python 3.8 walrus operator -> func return val gets added to list only if not null
    if activity := getActivity(wordWithoutPunctuation):
        if infoItems[-1].entityList:            
            return (State.NewItem, phrase, infoItems)
        
        infoItems[-1].activityList.append(activity)
        removeUnknownActivity(infoItems)
        infoItems[-1].addToRawSourceText(word)
        return (State.Activity, remainingPhrase, infoItems)
    
    # edge case ... pls tell me if you know a better solution
    if "allgemeiner beifall" in infoItems[-1].rawSourceText.lower():
        for partyName in ["ÖVP", "SPÖ", "FPÖ", "GRÜNE", "NEOS"]: # todo make this dynamically
            infoItems[-1].entityList.append(Entity("politicalParty", partyName)) 
    
    return (State.DetermineWordMeaning, phrase, infoItems) 

def entity_PoliticalParty(**kwds):
    phrase, infoItems = unpackPhraseAndInfoItems(kwds)
    word, remainingPhrase = getFirstWord(phrase)         
    isInterjectionFollowing = word.endswith(":")    
    wordWithoutPunctuation = stripPunctuation(word)
    
    if isFillerWord(wordWithoutPunctuation) or isWordOfType(Wordtype.CONNECTING_WORDS, wordWithoutPunctuation):
        infoItems[-1].addToRawSourceText(word)
        return (State.EntityPoliticalParty, remainingPhrase, infoItems)
    
    if entity := detectPoliticalPartyAbr(wordWithoutPunctuation):
        entityInstance = Entity("politicalParty", entity)
        infoItems[-1].entityList.append(entityInstance) 

    if isInterjectionFollowing:
        infoItems[-1].addToRawSourceText(word)
        return (State.Interjection, remainingPhrase, infoItems)
    elif entity:
        infoItems[-1].addToRawSourceText(word)
        return (State.EntityPoliticalParty, remainingPhrase, infoItems) 
    
    return (State.DetermineWordMeaning, phrase, infoItems)   

def entity_PersonOrPeople(**kwds):
    phrase, infoItems = unpackPhraseAndInfoItems(kwds)
    validPersonNames = cleanStringList(kwds["validPersonNames"])
    word, remainingPhrase = getFirstWord(phrase)
    wordWithoutPunctuation = stripPunctuation(word)    
        
    # detect descriptive behaviour of speaker
    if word == "–" and "–:" in remainingPhrase and not "–" in remainingPhrase[:remainingPhrase.index("–:")]:
        # e.g. "Abg. Leichtfried – in Richtung des das Red­nerpult verlassenden Abg. Scherak –: Also die Rede war jetzt in Ordnung!"
        infoItems[-1].addToRawSourceText(word)
        return (State.BehaviourDescription, remainingPhrase, infoItems)
    elif word == "–" or word == "":
        return (State.DetermineWordMeaning, phrase, infoItems)
    
    entity = detectPoliticalPartyAbr(wordWithoutPunctuation)    
    if entity:
        # some persons of a political party
        entityInstance = Entity("somePersonsOfPoliticalParty", entity)
        infoItems[-1].entityList.append(entityInstance)
          
    for name in validPersonNames:
        if phrase.lower().startswith(name.lower()):
            entityInstance = Entity("person", name)
            infoItems[-1].entityList.append(entityInstance)
            break           

    if word.endswith(":"):
        infoItems[-1].addToRawSourceText(word)
        return (State.Interjection, remainingPhrase, infoItems)
    
    infoItems[-1].addToRawSourceText(word)
    return (State.EntityPersonOrPeople, remainingPhrase, infoItems)
        
def behaviourDescription(**kwds):
    phrase, infoItems = unpackPhraseAndInfoItems(kwds)
    word, remainingPhrase = getFirstWord(phrase) 
    infoItems[-1].addToRawSourceText(word)
    if word.endswith("–:"):
        return (State.Interjection, remainingPhrase, infoItems)
    
    infoItems[-1].description = appendWordToPhrase(infoItems[-1].description, word)
    return (State.BehaviourDescription, remainingPhrase, infoItems)

def interjection(**kwds):
    phrase, infoItems = unpackPhraseAndInfoItems(kwds)
    word, remainingPhrase = getFirstWord(phrase)
    if word == "" or word == "–":
        return (State.DetermineWordMeaning, phrase, infoItems)

    infoItems[-1].quote = appendWordToPhrase(infoItems[-1].quote, word)
    
    # add item to list if not there already
    if "shouting" not in infoItems[-1].activityList:
        infoItems[-1].activityList.append("shouting")        
        removeUnknownActivity(infoItems)
    infoItems[-1].addToRawSourceText(word)
    return (State.Interjection, remainingPhrase, infoItems)

def removeUnknownActivity(infoItems):
    if "unknown" in infoItems[-1].activityList:
        infoItems[-1].activityList.remove("unknown")
