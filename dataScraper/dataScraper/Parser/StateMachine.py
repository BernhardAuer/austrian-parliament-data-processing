import InfoItem

# https://python-course.eu/applications-python/finite-state-machine.php
class StateMachine:
    
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, infoItems=None, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            raise InitializationError("at least one state must be an end_state")

        infoItems = [InfoItem]
        i = 0
        while True:
            i += 1
            if (i > 1000):
                print("detected potentially endless loop. abort parsing.")
                return
            (newState, cargo, infoItems) = handler(cargo, infoItems)
            if newState.upper() in self.endStates:
                print("reached ", newState)
                for infoItem in infoItems:
                    print("New ITEM:")
                    print(infoItem)
                    print("----------------------")
                break 
            else:
                
                print("currently ", newState)
                print("TEXT:", cargo)
                # print(infoItems[-1])
                handler = self.handlers[newState.upper()]   