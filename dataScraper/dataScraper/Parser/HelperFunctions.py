import string
from WordType import * 

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
    # strip any punctuation ...
    word = word.translate(str.maketrans('', '', string.punctuation))
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
