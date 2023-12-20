class InfoItem:
    def __init__(self):
        self.rawSourceText = "" # the orignial string, from which this item is beeing parsed
        self.subType = "" # ?? applause, ...
        self.activityList = [] # list of strings, eg. applause, cheerfulness, ... # todo: probably should be a set instead of list (prevent duplicate activities)
        self.entityList = [] # list of Entity() objects
        self.description = "" # further information/description about this parsed activity
        self.quote = "" # quote from the spoken shouts / speech from a person
    
    def __str__(self):
        return ("activityList: " + ",".join(self.activityList) 
        + ";\nentityList: \n" + ",\n".join([str(entityItem) for entityItem in self.entityList]) 
        + ";\nquote: " + self.quote
        + ";\ndescription: " + self.description
        + ";\nrawSourceText: " + self.rawSourceText)
    