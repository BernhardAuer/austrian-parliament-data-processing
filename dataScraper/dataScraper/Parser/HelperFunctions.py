import string
from dataScraper.Parser.WordType import * 

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
        "rufe": "shouting",
        "heiterkeit": "cheerfulness"
    }
    return activityDict.get(word.lower()) 
    
def detectPoliticalPartyAbr(word):
    word = stripPunctuation(word)
    entityDict = {
        "övp": "ÖVP",
        "fpö": "FPÖ",
        "spö": "SPÖ",
        "grünen": "GRÜNE",
        "grüne": "GRÜNE",
        "neos": "NEOS"
    }
    return entityDict.get(word.lower()) 

def isFillerWord(word):
    fillerWords = ["bei", "den", "der", "die", "das", "von", "des", "dem"]        
    return word in fillerWords

def getFirstWord(txt):
    splitted_txt = txt.split(maxsplit = 1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    return (word, txt)

def stripPunctuation(word):    
    return word.strip(string.punctuation)

def appendWordToPhrase(phrase, word):
    return phrase + word if phrase == "" else phrase + " " + word

def cleanStringList(list):
    result = []
    for string in list:
        s = string.strip()
        s = stripPunctuation(s) 
        if s and not s.isspace():       
            result.append(s)
    return result