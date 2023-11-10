
import re

class Wordtype:
    PRECEDING_Entity_WORDS = "precedingEntityWord"
    CONNECTING_WORDS = "connectingWords"
    
class StateMachineAction:
    DetectActivity = "DetectActivity"
    DetectConnectingWord = "DetectConnectingWord"
    DetectRestrictionOfEntity = "DetectRestrictionOfEntity"
    DetectEntityName = "DetectEntityName"
    ForceDetectEntityName = "ForceDetectEntityName"
    DetectActivityImplicit = "DetectActivityImplicit"
    DetectEnding = "DetectActivityImplicit"
    
    
class SpeechInfoParserStateMachine(object):
    def __init__(self):
        self.currentState = StateMachineAction.DetectActivity
        self.activityList = []
        self.entityList = []
        self.PersonOrPartsOfPartyAsEntityFollowing = False
        self.PersonNameSplitByWhitespace = False
        self.Speech = None
        self.PersonNameWithDash = False
    
    def isWordOfType(self, type, word):        
        connectingWordsList = ["und", ",", "sowie"]
        precedingEntityWordsList = ["abgeordnete","abg","abgeordneten"]
        match type:
            case Wordtype.CONNECTING_WORDS:
                if word.lower() in connectingWordsList:
                    return True    
            case Wordtype.PRECEDING_Entity_WORDS:
                if word.lower() in precedingEntityWordsList:
                    return True        
            case _: 
                print("unknown type!")            
        return False
    
    def getActivity(self, word):
        activityDict = {
            "beifall": "applause",
            "zwischenruf": "shout",
            "ruf": "shout",
            "heiterkeit": "cheerfulness"
        }
        return activityDict.get(word.lower()) 
    def getEntity(self, word):
        entityDict = {
            "övp": "övp",
            "fpö": "fpö",
            "spö": "spö",
            "grünen": "grüne",
            "grüne": "grüne",
            "neos": "neos"
        }
        return entityDict.get(word.lower()) 
    
    def removeFillerWords(self, input):
        fillerWords = ["bei", "den", "der", "die", "das", "von", "des", "dem"]
        for fillerWord in fillerWords:
            input = input.replace(fillerWord, "")
        return input
    
    def getRestrictionOfEntityName(self, word):
        keywordDict = [
            "abgeordnete",
            "abg",
            "abgeordneten"
        ]
    
    def doMatching(self, state, word):
        print("currentState:" + str(self.currentState))
        nextState = None
        match state:
            case StateMachineAction.DetectActivity:                    
                activity = self.getActivity(word)
                print(word + ": " + str(activity))
                if activity is not None:                    
                    self.activityList.append(activity)                    
                    nextState = StateMachineAction.DetectConnectingWord
                else:
                    self.currentState =  StateMachineAction.DetectRestrictionOfEntity 
                
            case StateMachineAction.DetectConnectingWord:           
                isConnectingWord = self.isWordOfType(Wordtype.CONNECTING_WORDS, word)
                print(word + ": " + str(isConnectingWord))
                if isConnectingWord:
                    nextState =  StateMachineAction.DetectActivity
                    self.PersonNameSplitByWhitespace = False # ensure that flag is reset, before parsing any further entities
                else:
                    self.currentState =  StateMachineAction.DetectRestrictionOfEntity    
                                        
            case StateMachineAction.DetectRestrictionOfEntity:  
                isEntityFollowing = self.isWordOfType(Wordtype.PRECEDING_Entity_WORDS, word)          
                
                print(word + ": " + str(isEntityFollowing))
                if isEntityFollowing:                    
                    self.PersonOrPartsOfPartyAsEntityFollowing = True
                    nextState =  StateMachineAction.DetectEntityName
                else:
                    self.currentState =  StateMachineAction.DetectEntityName
                      
            case StateMachineAction.DetectEntityName:
                if word == "–": # attention: gedankenstrich
                    nextState = "EndeImGelände"
                    return nextState
            
                if word == ":":
                    self.activityList.append("speech")
                    self.Speech = ""
                    nextState = "ParseSpeech"
                    return nextState
                    
                entity = self.getEntity(word)
                print(word + ": " + str(entity))
                if self.PersonOrPartsOfPartyAsEntityFollowing and entity is not None:
                    self.entityList.append("partsOf_" + str(entity)) # -> part of party
                    nextState =  StateMachineAction.DetectConnectingWord
                elif self.PersonOrPartsOfPartyAsEntityFollowing and entity is None and word == ".": # todo: better check if preceding word is abg
                    # -> person ATTENTION: there is this edge case: Abg. Brandstätter -> so we need to ignore the dot and parse person name in next iteration
                    nextState =  StateMachineAction.DetectEntityName
                elif self.PersonOrPartsOfPartyAsEntityFollowing and entity is None and self.PersonNameSplitByWhitespace:
                    if word == "-": # doppelname, zb, meinl-reisinger 
                        self.entityList[-1] = self.entityList[-1] + str(word) # -> person surname
                        self.PersonNameSplitByWhitespace = False
                        self.PersonNameWithDash = True
                    else:
                        self.entityList[-1] = self.entityList[-1] + " " + str(word) # -> person surname
                    nextState =  StateMachineAction.DetectConnectingWord                
                elif self.PersonOrPartsOfPartyAsEntityFollowing and entity is None and self.PersonNameWithDash:
                    if word == "-": # doppelname, zb, meinl-reisinger                         
                        self.PersonNameWithDash = True
                    self.PersonNameWithDash = False       
                    self.entityList[-1] = self.entityList[-1] + str(word) # -> person name with dash                                  
                    nextState =  StateMachineAction.DetectConnectingWord   
                elif self.PersonOrPartsOfPartyAsEntityFollowing and entity is None:
                    self.entityList.append("person_" + str(word)) # -> person
                    self.PersonNameSplitByWhitespace = True
                    nextState =  StateMachineAction.DetectConnectingWord
                elif entity is not None:                    
                    self.entityList.append(entity) # -> whole party
                    nextState =  StateMachineAction.DetectConnectingWord
                else:
                    self.currentState =  StateMachineAction.DetectActivityImplicit # no entity detected     
                
            case StateMachineAction.DetectActivityImplicit: 
                if word == ":":
                    self.activityList.append("speech")
                    self.Speech = ""
                    nextState = "ParseSpeech"
                
            case "ParseSpeech":                 
                print(word )
                if self.Speech == "" or re.match("[^\w\s]", word):
                    self.Speech += word # punctuation or first word of sentence ...
                else:
                    self.Speech += " " + word # whitespace before word
                if word == "–": # attention: gedankenstrich
                    nextState = "EndeImGelände"
                    return nextState
                nextState = "ParseSpeech"
                
                
            # case StateMachineAction.DetectEnding:            
            #     if word == "." or word == "–":
            #         nextState = "EndeImGelände"
                    
            case _:
                print("nix da!!!!!!!!")
                nextState = "Finished!!"
        return nextState
    
    def doParsing(self, input):
        # 1 todo clean and 3) füllwörter entfernen
        inputWithoutFillerWords = self.removeFillerWords(input)
        print(inputWithoutFillerWords)
        listOfWordsAndPunctuation = re.findall(r"\w+|[^\w\s]", inputWithoutFillerWords, re.UNICODE) # see https://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation
        print(*listOfWordsAndPunctuation, sep='"\n"')     
        for word in listOfWordsAndPunctuation:
            nextState = None
            while nextState is None:
                nextState = self.doMatching(self.currentState, word)
            self.currentState = nextState
            
            
        print("geparste Aktivität:")
        print(self.activityList)
        print("geparste entitäten:")
        print(self.entityList)
        print("geparste rede:")
        print(self.Speech)
                 
       
       
       
       
test = SpeechInfoParserStateMachine()
test.doParsing("Beifall und Heiterkeit bei der FPÖ, ÖVP sowie bei Abgeordneten der SPÖ und den Grünen, dem Abg. Brandstätter und der Abgeordneten Cornellia Ecker. – Heiterkeit bei den Grünen und bei Abgeordneten der SPÖ. – Zwischenruf bei der SPÖ.")
# test.doParsing("Beifall bei den Grünen sowie der Abg. Cornelia Julia Ecker.")
# test.doParsing("Beifall bei den Grünen sowie der Abgeordneten Herr und Kucharowits.")
# test.doParsing("Abg. Meinl-Reisinger: Geh bitte, he! Das ist ein bisschen sehr überheblich!")


