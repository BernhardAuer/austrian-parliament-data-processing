from dataScraper.Parser.InfoItem import InfoItem 
from dataScraper.Parser.State import State
from dataScraper.Parser.StateMachine import StateMachine
from dataScraper.Parser.StateMachineTransistions import *

def initStateMachine():
    infoItem = [InfoItem()]
    m = StateMachine()
    m.set_start(State.Initialize)

    m.add_state(State.Initialize, initialize)
    m.add_state(State.DetermineWordMeaning, determineWordMeaning)
    m.add_state(State.Activity, activity, infoItem)
    m.add_state(State.EntityPersonOrPeople, entity_PersonOrPeople, infoItem)
    m.add_state(State.EntityPoliticalParty, entity_PoliticalParty, infoItem)
    m.add_state(State.BehaviourDescription, behaviourDescription, infoItem)
    m.add_state(State.Interjection, interjection, infoItem)
    m.add_state(State.NewItem, newItem, infoItem)
    m.add_state(State.Ending, None, infoItem, end_state=1)

    return m
