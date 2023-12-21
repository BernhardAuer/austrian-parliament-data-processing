from dataScraper.Parser.State import State
from dataScraper.Parser.StateMachine import StateMachine
from dataScraper.Parser.StateMachineTransitions import *

def initStateMachine():
    m = StateMachine()
    m.set_start(State.Initialize)

    m.add_state(State.Initialize, initialize)
    m.add_state(State.DetermineWordMeaning, determineWordMeaning)
    m.add_state(State.Activity, activity)
    m.add_state(State.EntityPersonOrPeople, entity_PersonOrPeople)
    m.add_state(State.EntityPoliticalParty, entity_PoliticalParty)
    m.add_state(State.BehaviourDescription, behaviourDescription)
    m.add_state(State.Interjection, interjection)
    m.add_state(State.NewItem, newItem)
    m.add_state(State.Ending, None, end_state=1)

    return m
