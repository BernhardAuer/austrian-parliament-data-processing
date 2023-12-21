# https://python-course.eu/applications-python/finite-state-machine.php
class StateMachine:
    
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, phrase, validPersonNames = []):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            raise InitializationError("at least one state must be an end_state")

        infoItems = None
        i = 0
        while True:
            i += 1
            if (i > 1000):
                print("detected a potential endless loop. abort parsing.") # todo: logger & warning
                return None
            (newState, phrase, infoItems) = handler(phrase = phrase, infoItems = infoItems, validPersonNames = validPersonNames)
            if newState.upper() in self.endStates:
                # for infoItem in infoItems:
                #     print("New ITEM:")
                #     print(infoItem)
                #     print("----------------------")
                return infoItems
            else:                
                # print("currently ", newState)
                # print("TEXT:", phrase)
                handler = self.handlers[newState.upper()]   