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
#m.run("Beifall und Heiterkeit bei der FPÖ, ÖVP sowie bei Abgeordneten der SPÖ und den Grünen, dem Abg. Brandstätter und der Abgeordneten Cornellia Ecker. – Heiterkeit bei den Grünen und bei Abgeordneten der SPÖ. – Zwischenruf bei der SPÖ.")
#m.run("Beifall bei den Grünen sowie der Abg. Cornelia Julia Ecker.")
#m.run("Beifall bei den Grünen sowie der Abgeordneten Herr und Kucharowits.")
#m.run("Abg. Meinl-Reisinger: Geh bitte, he! Das ist ein bisschen sehr überheblich!")
#m.run("Zwischenrufe der Abgeordneten Heinisch-Hosek und Kucharowits.")
#m.run("Abg. Ottenschläger: Das war jetzt sehr streng! – Beifall bei den Grünen sowie der Abgeordneten Herr und Kucharowits.")
#m.run("Abg. Ottenschläger: Das war jetzt sehr streng! – Weitere Rufe bei der ÖVP: Streng!")
#m.run("in die rechte Ecke zeigend")
#m.run("Allgemeiner Beifall. –     hallo, das ist ein test  –  und noch ein test")
#m.run("Abg. Leichtfried – in Richtung des das Rednerpult verlassenden Abg. Scherak –: Also die Rede war jetzt in Ordnung!")
#m.run("Zwischenruf des Abg. Hafenecker. – Abg. Stögmüller – in Richtung Abg. Hafenecker –: Für die Bevölkerung ist die Polizei zuständig, Herr Kollege! – Präsident Sobotka gibt das Glockenzeichen.")

# m.run("Heiterkeit und Beifall bei den Grünen sowie Beifall der Abg. Herr.")





#m.run("Beifall und Heiterkeit bei der FPÖ, ÖVP sowie bei Abgeordneten der SPÖ, Neos und den Grünen, dem Abg. Brandstätter und der Abgeordneten Cornellia Ecker.")
#m.run("Beifall bei den Grünen sowie der Abg. Cornelia Julia Ecker.")
#m.run("Beifall bei den Grünen sowie der Abgeordneten Herr und Kucharowits.")
 
# this needs to be unit tested!!!!!       
#m.run("Abg. Meinl-Reisinger: Geh bitte, he! – Abg. Stögmüller schneuzt sich – Zwischenruf von Abg. Hafenecker – Abg. Blah – na sowas –: Für die Bevölkerung ist die Polizei zuständig, Herr Kollege! – Präsident Sobotka gibt das Glockenzeichen.")
# todo: test multiple whitespaces