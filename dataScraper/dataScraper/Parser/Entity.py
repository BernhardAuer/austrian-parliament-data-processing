class Entity:
    def __init__(self, type, name):
        self.type = type # person, politicalParty, somePersonsOfPoliticalParty
        self.name = name    
    def __str__(self):
        return "Entity-type: " + self.type + "; name: " + self.name 
    def asDict(self):
        return {'type': self.type, 'name': self.name}
