import InfoItem 
import State
from StateMachine import StateMachine
from StateMachineTransistions import *

infoItem = [InfoItem()]
m = StateMachine()
m.set_start(State.Start)

m.add_state(State.Start, startTransitions)
m.add_state(State.Activity, activityTransitions, infoItem)
m.add_state(State.ActivityConnectingWord, activityConnectingWordTransistions, infoItem)
m.add_state(State.BeginningOfEntity, detectBeginningOfEntityTransistions, infoItem)
m.add_state(State.EntityPersonOrPeople, entityPersonOrPeopleTransistions, infoItem)
m.add_state(State.EntityPoliticalParty, entityPoliticalPartyTransistions, infoItem)
m.add_state(State.EntityPoliticalPartyConnectingWord, entityPoliticalPartyConnectingWordTransistions, infoItem)
m.add_state(State.EntityPersonOrPeopleConnectingWord, entityPersonOrPeopleConnectingWordTransistions, infoItem)
m.add_state(State.BehaviourDescription, speakerBehaviourDescriptionTransistions, infoItem)
m.add_state(State.ImplicitActivity, implicitActivityTransistions, infoItem)
m.add_state(State.Speech, speechTransistions, infoItem)
m.add_state(State.NewItem, newItemTransistions, infoItem)
m.add_state(State.Ending, None, infoItem, end_state=1)

m.run("Beifall und Heiterkeit bei der FPÖ, ÖVP sowie bei Abgeordneten der SPÖ und den Grünen, dem Abg. Brandstätter und der Abgeordneten Cornellia Ecker. – Heiterkeit bei den Grünen und bei Abgeordneten der SPÖ. – Zwischenruf bei der SPÖ.")
# doParsing("Beifall bei den Grünen sowie der Abg. Cornelia Julia Ecker.")
# doParsing("Beifall bei den Grünen sowie der Abgeordneten Herr und Kucharowits.")
#doParsing("Abg. Meinl-Reisinger: Geh bitte, he! Das ist ein bisschen sehr überheblich!")
#doParsing("Zwischenrufe der Abgeordneten Heinisch-Hosek und Kucharowits.")
#doParsing("Abg. Ottenschläger: Das war jetzt sehr streng! – Beifall bei den Grünen sowie der Abgeordneten Herr und Kucharowits.")
#doParsing("Abg. Ottenschläger: Das war jetzt sehr streng! – Weitere Rufe bei der ÖVP: Streng!")
#doParsing("in die rechte Ecke zeigend")
# doParsing("Allgemeiner Beifall. –  hallo, das ist ein test –  und noch ein test")
# doParsing("Abg. Leichtfried – in Richtung des das Rednerpult verlassenden Abg. Scherak –: Also die Rede war jetzt in Ordnung!")
# doParsing("Zwischenruf des Abg. Hafenecker. – Abg. Stögmüller – in Richtung Abg. Hafenecker –: Für die Bevölkerung ist die Polizei zuständig, Herr Kollege! – Präsident Sobotka gibt das Glockenzeichen.")

# doParsing("Heiterkeit und Beifall bei den Grünen sowie Beifall der Abg. Herr.")





#doParsing("Beifall und Heiterkeit bei der FPÖ, ÖVP sowie bei Abgeordneten der SPÖ, Neos und den Grünen, dem Abg. Brandstätter und der Abgeordneten Cornellia Ecker.")
#doParsing("Beifall bei den Grünen sowie der Abg. Cornelia Julia Ecker.")
#doParsing("Beifall bei den Grünen sowie der Abgeordneten Herr und Kucharowits.")
          