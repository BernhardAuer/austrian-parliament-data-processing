import copy
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
    DetectEnding = "DetectEnding"
    
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
    
class SpeechInfoParserStateMachine(object):
    def __init__(self):
        self.currentState = StateMachineAction.DetectActivity
        self.activityList = []
        self.entityList = []
        self.PersonOrPartsOfPartyAsEntityFollowing = False
        self.PersonNameSplitByWhitespace = False
        self.Speech = None
        self.PersonNameWithDash = False
        self.InfoItem = InfoItem()
        self.ResultList = []
    
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
            "zwischenruf": "shouting",
            "zwischenrufe": "shouting",
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
    
    def isFillerWord(self, word):
        fillerWords = ["bei", "den", "der", "die", "das", "von", "des", "dem"]        
        return word in fillerWords
    
    def getRestrictionOfEntityName(self, word):
        keywordDict = [
            "abgeordnete",
            "abg",
            "abgeordneten"
        ]
    
    def doMatching(self, state, word, precedingWord, isLastWord, fullWordsList, index):
        print("***currentState:" + str(self.currentState) + " CurrentWord: " + word + " isLastWord?: " + str(isLastWord))
        if self.isFillerWord(word) and self.currentState is not "ParseSpeech" and self.currentState is not "ParseBehaviourOfSpeaker":
            print("skip, weil fillerWord!" + word)
            nextState = self.currentState
            return nextState
        
        nextState = None
        match state:
            case StateMachineAction.DetectActivity:                    
                activity = self.getActivity(word)
                print(word + ": " + str(activity))
                if activity is not None and self.InfoItem.activityList and self.InfoItem.entityList: 
                    self.currentState = "EndAndStartNewParsing"
                    return
                elif activity is not None:
                    self.InfoItem.activityList.append(activity)                    
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
                    print("gedankenstrich...")
                    # edge case: description before speech e.g.:Abg. Leichtfried – in Richtung des das Red­nerpult verlassenden Abg. Scherak –: Also die Rede war jetzt in Ordnung!
                    remainingWords = fullWordsList[index + 1:]
                    print(remainingWords)
                    for j,w in enumerate(remainingWords):
                        if w == "–":
                            if remainingWords[j + 1] == ":": 
                                # parse description before speech
                                nextState = "ParseBehaviourOfSpeaker"
                                return nextState
                            else:
                                break 
                    self.currentState = StateMachineAction.DetectEnding
                    return
            
                if word == ":":
                    self.InfoItem.activityList.append("shouting")
                    self.InfoItem.quote = ""
                    self.Speech = ""
                    nextState = "ParseSpeech"
                    return nextState
                    
                entity = self.getEntity(word)
                print(word + ": " + str(entity))
                if self.PersonOrPartsOfPartyAsEntityFollowing and entity is not None:
                    entityInstance = Entity("somePersonsOfPoliticalParty", entity)
                    self.InfoItem.entityList.append(entityInstance)
                    nextState =  StateMachineAction.DetectConnectingWord
                elif self.PersonOrPartsOfPartyAsEntityFollowing and entity is None and word == ".": # todo: better check if preceding word is abg
                    # -> person ATTENTION: there is this edge case: Abg. Brandstätter -> so we need to ignore the dot and parse person name in next iteration
                    nextState =  StateMachineAction.DetectEntityName
                elif self.PersonOrPartsOfPartyAsEntityFollowing and entity is None and self.PersonNameSplitByWhitespace:
                    if word == "-": # doppelname, zb, meinl-reisinger 
                        updatedName = self.InfoItem.entityList[-1].name + str(word) # -> person surname
                        self.InfoItem.entityList[-1].name = updatedName
                        self.entityList[-1] = self.entityList[-1] + str(word) # -> person surname  
                        self.PersonNameSplitByWhitespace = False
                        self.PersonNameWithDash = True
                    else:
                        self.entityList[-1] = self.entityList[-1] + " " + str(word) # -> person surname
                        updatedName = self.InfoItem.entityList[-1].name + " " + str(word) # -> person surname
                        self.InfoItem.entityList[-1].name = updatedName
                    nextState =  StateMachineAction.DetectConnectingWord                
                elif self.PersonOrPartsOfPartyAsEntityFollowing and entity is None and self.PersonNameWithDash:
                    if word == "-": # doppelname, zb, meinl-reisinger                         
                        self.PersonNameWithDash = True
                    self.PersonNameWithDash = False                      
                    self.InfoItem.entityList[-1].name = self.InfoItem.entityList[-1].name + str(word) 
                    self.entityList[-1] = self.entityList[-1] + str(word) # -> person name with dash                                  
                    nextState =  StateMachineAction.DetectConnectingWord   
                elif self.PersonOrPartsOfPartyAsEntityFollowing and entity is None:
                    self.entityList.append("person_" + str(word)) # -> person
                    entityInstance = Entity("person", word)
                    self.InfoItem.entityList.append(entityInstance)
                    self.PersonNameSplitByWhitespace = True
                    nextState =  StateMachineAction.DetectConnectingWord
                elif entity is not None:     
                    entityInstance = Entity("politicalParty", entity)
                    self.InfoItem.entityList.append(entityInstance) 
                    nextState =  StateMachineAction.DetectConnectingWord
                else:
                    self.currentState =  StateMachineAction.DetectActivityImplicit # no entity detected     
                
            case StateMachineAction.DetectActivityImplicit: 
                if word == ":":
                    self.InfoItem.activityList.append("shouting")
                    self.InfoItem.quote = ""
                    self.activityList.append("speech")
                    self.Speech = ""
                    nextState = "ParseSpeech"
                else:
                    self.currentState = StateMachineAction.DetectEnding
                   
            case "ParseSpeech":                             
                if word == "–": # attention: gedankenstrich
                    self.currentState = StateMachineAction.DetectEnding
                    return 
                quote = self.InfoItem.quote
                if quote == "" or re.match("[^\w\s]", word):
                    quote += word # punctuation or first word of sentence ...
                else:
                    quote += " " + word # whitespace before word
                    
                self.InfoItem.quote = quote
                
                nextState = "ParseSpeech"
                
                                
            case "ParseBehaviourOfSpeaker":
                if word == "–" and fullWordsList[index + 1] == ":":
                    print("next: ParseSpeech")
                    nextState = StateMachineAction.DetectActivityImplicit
                    return nextState
                if self.InfoItem.description == "":
                    self.InfoItem.description = word
                else: 
                    self.InfoItem.description += " " + word
                nextState="ParseBehaviourOfSpeaker"
                        
            case StateMachineAction.DetectEnding:  
                print(word)
                                
                endingWords = ["–"] 
                # detect ending
                if isLastWord or word in endingWords:
                    print("ending of current Item")
                    
                    # detect edge cases ...
                    if "allgemeiner beifall" in self.InfoItem.rawSourceText.lower():
                        print("applause by every party edge case ....")
                        for partyName in ["övp", "spö", "fpö", "grüne", "neos"]: # todo make this dynamically
                            self.InfoItem.entityList.append(Entity("politicalParty", partyName)) 
                    self.currentState = "Ending"
                    return
                else:
                    nextState = StateMachineAction.DetectActivity
                    return nextState
                
            case "Ending":    
                # ending detected 
                if not self.InfoItem.activityList: # list is empty -> no valid activity could be parsed # todo: fix bug for very last item with no activity
                    self.InfoItem.activityList.append("unknown")
                
                # convert to dict because of mongoDB
                convertedList = []
                for entity in self.InfoItem.entityList:
                    convertedList.append(entity.asDict())                    
                self.InfoItem.entityList = convertedList
                
                self.ResultList.append(copy.deepcopy(self.InfoItem))
                print(self.InfoItem)
                self.InfoItem = InfoItem()
                self.currentState =  StateMachineAction.DetectActivity
                # todo: maybe just re-instanciate this StateMachineObject? so no wrong states could be persisted
                self.PersonOrPartsOfPartyAsEntityFollowing = False
                self.PersonNameSplitByWhitespace = False
                self.Speech = None
                self.PersonNameWithDash = False
                nextState = StateMachineAction.DetectActivity # start from beginning?
                
            case "EndAndStartNewParsing":    
                # ending detected 
                if not self.InfoItem.activityList: # list is empty -> no valid activity could be parsed # todo: fix bug for very last item with no activity
                    self.InfoItem.activityList.append("unknown")
                
                # convert to dict because of mongoDB
                convertedList = []
                for entity in self.InfoItem.entityList:
                    convertedList.append(entity.asDict())                    
                self.InfoItem.entityList = convertedList
                
                self.ResultList.append(copy.deepcopy(self.InfoItem))
                print(self.InfoItem)
                self.InfoItem = InfoItem()
                self.currentState =  StateMachineAction.DetectActivity
                # todo: maybe just re-instanciate this StateMachineObject? so no wrong states could be persisted
                self.PersonOrPartsOfPartyAsEntityFollowing = False
                self.PersonNameSplitByWhitespace = False
                self.Speech = None
                self.PersonNameWithDash = False
                return                  
                  
            case _:
                print("nix da error!!!!!!!!")
                nextState = "error!!"
        return nextState
    
    def doParsing(self, input):
        # 1 todo clean 
        # print(inputWithoutFillerWords)
        listOfWordsAndPunctuation = re.findall(r"\w+|[^\w\s]", input, re.UNICODE) # see https://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation
        print(*listOfWordsAndPunctuation, sep='"\n"')   
        endingIndex = len(listOfWordsAndPunctuation) - 1  
        for index, word in enumerate(listOfWordsAndPunctuation):
            isLastWord = False
            if index == endingIndex:
                isLastWord = True
                        
            precedingWord = listOfWordsAndPunctuation[index - 1]
            nextState = None
            while nextState is None:
                nextState = self.doMatching(self.currentState, word, precedingWord, isLastWord, listOfWordsAndPunctuation, index)
            
            self.addWordToRawSourceText(word) # add this after "successfull" parse, to ensure that raw-text gets added to the correct item
            self.currentState = nextState    
               
    
        # convert to dict because of mongoDB
        convertedList = []
        for entity in self.InfoItem.entityList:
            convertedList.append(entity.asDict())                    
        self.InfoItem.entityList = convertedList 
        # add last item? duplicate edge case?
        self.ResultList.append(copy.deepcopy(self.InfoItem))
                
        return self.ResultList                
        # print("geparste Aktivität:")
        # print(self.activityList)
        # print("geparste entitäten:")
        # print(self.entityList)
        # print("geparste rede:")
        # print(self.Speech)
        # print("-----------------")
        # for result in self.ResultList:
        #     print("\nITEM:")
        #     print(result)

    def addWordToRawSourceText(self, word):
        if self.InfoItem.rawSourceText == "" or re.match("[^\w\s]", word):
            self.InfoItem.rawSourceText += word
        else:
            self.InfoItem.rawSourceText += " " + word
                 
       
       
       
       
# test = SpeechInfoParserStateMachine()
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