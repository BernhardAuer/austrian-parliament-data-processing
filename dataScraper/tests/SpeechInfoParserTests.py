import unittest
from dataScraper.Parser.InitStateMachine import initStateMachine
from dataScraper.Parser.InfoItem import InfoItem
from dataScraper.Parser.Entity import Entity

class SpeechInfoParserTests(unittest.TestCase):

    def setUp(self):
        self.fsm = initStateMachine()

    def test_run_unknownTextGiven_shouldReturnItemWithUnknownActivity(self):
        # arrange
        expectedRawSourceText = "Präsident Sobotka gibt das Glockenzeichen."
        expectedActivityListItem = "unknown"
             
        # execute
        results = self.fsm.run("Präsident Sobotka gibt das Glockenzeichen.")
        
        # assert
        self.assertEqual(len(results), 1)
        result = results[0]
        self.assertEqual(result.rawSourceText, expectedRawSourceText)
        self.assertEqual(result.description, "")
        self.assertEqual(result.quote, "")
        self.assertEqual(len(result.activityList), 1)
        self.assertEqual(result.activityList[0], expectedActivityListItem)
        self.assertEqual(len(result.entityList), 0)
        
    def test_run_applauseByPartyAndPerson_shouldReturnItemWithApplauseActivityAndEntities(self):
        # arrange
        expectedRawSourceText = "Beifall bei den Grünen sowie der Abg. Musterfrau."
        expectedActivityListItem = "applause"
        expectedPartyEntity = Entity("politicalParty", "grüne")        
        expectedPersonEntity = Entity("person", "Musterfrau")
             
        # execute
        results = self.fsm.run("Beifall bei den Grünen sowie der Abg. Musterfrau.")
        
        # assert
        self.assertEqual(len(results), 1)
        result = results[0]
        
        self.assertEqual(result.rawSourceText, expectedRawSourceText)
        self.assertEqual(result.description, "")
        self.assertEqual(result.quote, "")
        self.assertEqual(len(result.activityList), 1)
        self.assertEqual(result.activityList[0], expectedActivityListItem)
        
        self.assertEqual(len(result.entityList), 2)
        self.assertEqual(result.entityList[0].type, expectedPartyEntity.type)
        self.assertEqual(result.entityList[0].name, expectedPartyEntity.name)
        self.assertEqual(result.entityList[1].type, expectedPersonEntity.type)
        self.assertEqual(result.entityList[1].name, expectedPersonEntity.name)
        
    def test_run_singleActivityByMultipleEntities_shouldReturnParsedItem(self):
        # arrange
        expectedRawSourceText = "Beifall bei den Grünen, bei Abgeordneten der ÖVP, NEOS und der FPÖ sowie der Abgeordneten Herr und Kucharowits."
        expectedActivityListItem = "applause"
        expectedPartyEntity = Entity("politicalParty", "grüne")   
        expectedPeopleOfPartyEntity1 = Entity("somePersonsOfPoliticalParty", "övp")  
        expectedPeopleOfPartyEntity2 = Entity("somePersonsOfPoliticalParty", "neos")  
        expectedPeopleOfPartyEntity3 = Entity("somePersonsOfPoliticalParty", "fpö")        
        expectedPersonEntity1 = Entity("person", "Herr")       
        expectedPersonEntity2 = Entity("person", "Kucharowits")
             
        # execute
        results = self.fsm.run("Beifall bei den Grünen, bei Abgeordneten der ÖVP, NEOS und der FPÖ sowie der Abgeordneten Herr und Kucharowits.")
        
        # assert
        self.assertEqual(len(results), 1)
        result = results[0]
        
        self.assertEqual(result.rawSourceText, expectedRawSourceText)
        self.assertEqual(result.description, "")
        self.assertEqual(result.quote, "")
        self.assertEqual(len(result.activityList), 1)
        self.assertEqual(result.activityList[0], expectedActivityListItem)
        
        self.assertEqual(len(result.entityList), 6)
        self.assertEqual(result.entityList[0].type, expectedPartyEntity.type)
        self.assertEqual(result.entityList[0].name, expectedPartyEntity.name)
        self.assertEqual(result.entityList[1].type, expectedPeopleOfPartyEntity1.type)
        self.assertEqual(result.entityList[1].name, expectedPeopleOfPartyEntity1.name)
        self.assertEqual(result.entityList[2].type, expectedPeopleOfPartyEntity2.type)
        self.assertEqual(result.entityList[2].name, expectedPeopleOfPartyEntity2.name)
        self.assertEqual(result.entityList[3].type, expectedPeopleOfPartyEntity3.type)
        self.assertEqual(result.entityList[3].name, expectedPeopleOfPartyEntity3.name)
        self.assertEqual(result.entityList[4].type, expectedPersonEntity1.type)
        self.assertEqual(result.entityList[4].name, expectedPersonEntity1.name)
        self.assertEqual(result.entityList[5].type, expectedPersonEntity2.type)
        self.assertEqual(result.entityList[5].name, expectedPersonEntity2.name)
        
    def test_run_multipleActivitiesByMultipleEntities_shouldReturnParsedItem(self):
        # arrange
        expectedRawSourceText = "Heiterkeit und Beifall bei den Grünen sowie der Abg. Herr."
        expectedActivityListItem1 = "cheerfulness"
        expectedActivityListItem2 = "applause"
        expectedPartyEntity = Entity("politicalParty", "grüne")        
        expectedPersonEntity = Entity("person", "Herr")
             
        # execute
        results = self.fsm.run("Heiterkeit und Beifall bei den Grünen sowie der Abg. Herr.")
        
        # assert
        self.assertEqual(len(results), 1)
        result = results[0]
        
        self.assertEqual(result.rawSourceText, expectedRawSourceText)
        self.assertEqual(result.description, "")
        self.assertEqual(result.quote, "")
        self.assertEqual(len(result.activityList), 2)
        self.assertEqual(result.activityList[0], expectedActivityListItem1)
        self.assertEqual(result.activityList[1], expectedActivityListItem2)
        
        self.assertEqual(len(result.entityList), 2)
        self.assertEqual(result.entityList[0].type, expectedPartyEntity.type)
        self.assertEqual(result.entityList[0].name, expectedPartyEntity.name)
        self.assertEqual(result.entityList[1].type, expectedPersonEntity.type)
        self.assertEqual(result.entityList[1].name, expectedPersonEntity.name)
    
    def test_run_differentActivitiesByDifferentEntitiesInSamePhrase_shouldReturnParsedItem(self):
        # arrange
        expectedActivityListItem1 = "cheerfulness"
        expectedActivityListItem2 = "applause"
        expectedPartyEntity = Entity("politicalParty", "grüne")        
        expectedPersonEntity = Entity("person", "Herr")
             
        # execute
        results = self.fsm.run("Heiterkeit und Beifall bei den Grünen sowie Beifall der Abg. Herr.")
        
        # assert
        self.assertEqual(len(results), 2)
        
        self.assertEqual(results[0].rawSourceText, "Heiterkeit und Beifall bei den Grünen sowie")
        self.assertEqual(results[0].description, "")
        self.assertEqual(results[0].quote, "")
        self.assertEqual(len(results[0].activityList), 2)
        self.assertEqual(results[0].activityList[0], expectedActivityListItem1)
        self.assertEqual(results[0].activityList[1], expectedActivityListItem2)
        
        self.assertEqual(len(results[0].entityList), 1)
        self.assertEqual(results[0].entityList[0].type, expectedPartyEntity.type)
        self.assertEqual(results[0].entityList[0].name, expectedPartyEntity.name)
        
                
        self.assertEqual(results[1].rawSourceText, "Beifall der Abg. Herr.")
        self.assertEqual(results[1].description, "")
        self.assertEqual(results[1].quote, "")
        self.assertEqual(len(results[1].activityList), 1)
        self.assertEqual(results[1].activityList[0], expectedActivityListItem2)
        
        self.assertEqual(len(results[1].entityList), 1)
        self.assertEqual(results[1].entityList[0].type, expectedPersonEntity.type)
        self.assertEqual(results[1].entityList[0].name, expectedPersonEntity.name)    
     
    def test_run_interjectionByPersonWithoutBehaviourDescription_shouldReturnParsedItem(self):
        # arrange
        expectedRawSourceText = "Abg. Meinl: Geh bitte, he! Das ist ein bisschen sehr überheblich!"
        expectedActivityListItem = "shouting"     
        expectedPersonEntity = Entity("person", "Meinl")
             
        # execute
        results = self.fsm.run("Abg. Meinl: Geh bitte, he! Das ist ein bisschen sehr überheblich!")
        
        # assert
        self.assertEqual(len(results), 1)
        result = results[0]
        
        self.assertEqual(result.rawSourceText, expectedRawSourceText)
        self.assertEqual(result.description, "")
        self.assertEqual(result.quote, "Geh bitte, he! Das ist ein bisschen sehr überheblich!")
        self.assertEqual(len(result.activityList), 1)
        self.assertEqual(result.activityList[0], expectedActivityListItem)
        
        self.assertEqual(len(result.entityList), 1)
        self.assertEqual(result.entityList[0].type, expectedPersonEntity.type)
        self.assertEqual(result.entityList[0].name, expectedPersonEntity.name)
          
    def test_run_interjectionByPersonWithBehaviourDescription_shouldReturnParsedItem(self):
        # arrange
        expectedRawSourceText = "Abg. Leichtfried – in Richtung des das Rednerpult verlassenden Abg. Scherak –: Also die Rede war jetzt in Ordnung!"
        expectedActivityListItem = "shouting"     
        expectedPersonEntity = Entity("person", "Leichtfried")
             
        # execute
        results = self.fsm.run("Abg. Leichtfried – in Richtung des das Rednerpult verlassenden Abg. Scherak –: Also die Rede war jetzt in Ordnung!")
        
        # assert
        self.assertEqual(len(results), 1)
        result = results[0]
        
        self.assertEqual(result.rawSourceText, expectedRawSourceText)
        self.assertEqual(result.description, "in Richtung des das Rednerpult verlassenden Abg. Scherak")
        self.assertEqual(result.quote, "Also die Rede war jetzt in Ordnung!")
        self.assertEqual(len(result.activityList), 1)
        self.assertEqual(result.activityList[0], expectedActivityListItem)
        
        self.assertEqual(len(result.entityList), 1)
        self.assertEqual(result.entityList[0].type, expectedPersonEntity.type)
        self.assertEqual(result.entityList[0].name, expectedPersonEntity.name)
    
    def test_run_interjectionWithoutQuote_shouldReturnParsedItem(self):
        # arrange
        expectedRawSourceText = "Zwischenrufe der Abgeordneten Heinisch und Kucharowits."
        expectedActivityListItem = "shouting"
        expectedPersonEntity1 = Entity("person", "Heinisch")
        expectedPersonEntity2 = Entity("person", "Kucharowits")
        
        # execute
        results = self.fsm.run("Zwischenrufe der Abgeordneten Heinisch und Kucharowits.")
        
        # assert
        self.assertEqual(len(results), 1)
        result = results[0]
        
        self.assertEqual(result.rawSourceText, expectedRawSourceText)
        self.assertEqual(result.description, "")
        self.assertEqual(result.quote, "")
        self.assertEqual(len(result.activityList), 1)
        self.assertEqual(result.activityList[0], expectedActivityListItem)
        
        self.assertEqual(len(result.entityList), 2)
        self.assertEqual(result.entityList[0].type, expectedPersonEntity1.type)
        self.assertEqual(result.entityList[0].name, expectedPersonEntity1.name)
        self.assertEqual(result.entityList[1].type, expectedPersonEntity2.type)
        self.assertEqual(result.entityList[1].name, expectedPersonEntity2.name)

    def test_run_personNameWithDash_shouldReturnParsedItem(self):
        # arrange
        expectedRawSourceText = "Zwischenruf der Abgeordneten Heinisch-Hosek."
        expectedActivityListItem = "shouting"
        expectedPersonEntity1 = Entity("person", "Heinisch-Hosek")
        
        # execute
        results = self.fsm.run("Zwischenruf der Abgeordneten Heinisch-Hosek.")
        
        # assert
        self.assertEqual(len(results), 1)
        result = results[0]
        
        self.assertEqual(result.rawSourceText, expectedRawSourceText)
        self.assertEqual(result.description, "")
        self.assertEqual(result.quote, "")
        self.assertEqual(len(result.activityList), 1)
        self.assertEqual(result.activityList[0], expectedActivityListItem)
        
        self.assertEqual(len(result.entityList), 1)
        self.assertEqual(result.entityList[0].type, expectedPersonEntity1.type)
        self.assertEqual(result.entityList[0].name, expectedPersonEntity1.name)

    def test_run_phraseWithMultipleIndependentEvents_shouldReturnMultipleItems(self):
        # arrange
        expectedActivityListItem1 = "cheerfulness"
        expectedActivityListItem2 = "shouting"
        expectedEntity1 = Entity("politicalParty", "grüne")
        expectedEntity2 = Entity("somePersonsOfPoliticalParty", "spö")
        expectedEntity3 = Entity("politicalParty", "spö")
        
        # execute
        results = self.fsm.run("Heiterkeit bei den Grünen und bei Abgeordneten der SPÖ. – Zwischenruf bei der SPÖ.")
        
        # assert
        self.assertEqual(len(results), 2)
        
        self.assertEqual(results[0].rawSourceText, "Heiterkeit bei den Grünen und bei Abgeordneten der SPÖ.")
        self.assertEqual(results[0].description, "")
        self.assertEqual(results[0].quote, "")
        self.assertEqual(len(results[0].activityList), 1)
        self.assertEqual(results[0].activityList[0], expectedActivityListItem1)        
        self.assertEqual(len(results[0].entityList), 2)
        self.assertEqual(results[0].entityList[0].type, expectedEntity1.type)
        self.assertEqual(results[0].entityList[0].name, expectedEntity1.name)
        self.assertEqual(results[0].entityList[1].type, expectedEntity2.type)
        self.assertEqual(results[0].entityList[1].name, expectedEntity2.name)
        
        self.assertEqual(results[1].rawSourceText, "Zwischenruf bei der SPÖ.")
        self.assertEqual(results[1].description, "")
        self.assertEqual(results[1].quote, "")
        self.assertEqual(len(results[1].activityList), 1)
        self.assertEqual(results[1].activityList[0], expectedActivityListItem2)        
        self.assertEqual(len(results[1].entityList), 1)
        self.assertEqual(results[1].entityList[0].type, expectedEntity3.type)
        self.assertEqual(results[1].entityList[0].name, expectedEntity3.name)

    def test_run_phraseWithManyWhitespacesBetweenIndent_shouldReturnMultipleItemsWithContent(self):
        # arrange
        expectedEntity1 = Entity("politicalParty", "spö")
        
        # execute
        results = self.fsm.run("Beifall der SPÖ. –     hallo, das ist ein test  –  und noch ein test")
        
        # assert
        self.assertEqual(len(results), 3)
        
        self.assertEqual(results[0].rawSourceText, "Beifall der SPÖ.")
        self.assertEqual(results[0].description, "")
        self.assertEqual(results[0].quote, "")
        self.assertEqual(len(results[0].activityList), 1)
        self.assertEqual(results[0].activityList[0], "applause")        
        self.assertEqual(len(results[0].entityList), 1)
        self.assertEqual(results[0].entityList[0].type, expectedEntity1.type)
        self.assertEqual(results[0].entityList[0].name, expectedEntity1.name)
        
        self.assertEqual(results[1].rawSourceText, "hallo, das ist ein test")
        self.assertEqual(results[1].description, "")
        self.assertEqual(results[1].quote, "")
        self.assertEqual(len(results[1].activityList), 1)
        self.assertEqual(results[1].activityList[0], "unknown")        
        self.assertEqual(len(results[1].entityList), 0)
        
        self.assertEqual(results[2].rawSourceText, "und noch ein test")
        self.assertEqual(results[2].description, "")
        self.assertEqual(results[2].quote, "")
        self.assertEqual(len(results[2].activityList), 1)
        self.assertEqual(results[2].activityList[0], "unknown")        
        self.assertEqual(len(results[2].entityList), 0)


    def test_run_interjectionByPoliticalParty_shouldReturnItem(self):
        # arrange
        expectedEntity1 = Entity("politicalParty", "övp")
        
        # execute
        results = self.fsm.run("Weitere Rufe bei der ÖVP: Streng!")
        
        # assert
        self.assertEqual(len(results), 1)
        
        self.assertEqual(results[0].rawSourceText, "Weitere Rufe bei der ÖVP: Streng!")
        self.assertEqual(results[0].description, "")
        self.assertEqual(results[0].quote, "Streng!")
        self.assertEqual(len(results[0].activityList), 1)
        self.assertEqual(results[0].activityList[0], "shouting")        
        self.assertEqual(len(results[0].entityList), 1)
        self.assertEqual(results[0].entityList[0].type, expectedEntity1.type)
        self.assertEqual(results[0].entityList[0].name, expectedEntity1.name)
        
    # todo: this needs to be fixed!!!!
    def test_run_personFullNameWithWhitespaces_shouldReturnItem(self):
        # arrange
        expectedEntity1 = Entity("person", "Cornelia")
        expectedEntity2 = Entity("person", "Julia")
        expectedEntity3 = Entity("person", "Ecker")
        
        # execute
        results = self.fsm.run("Beifall bei der Abg. Cornelia Julia Ecker.")
        
        # assert
        self.assertEqual(len(results), 1)
        
        self.assertEqual(results[0].rawSourceText, "Beifall bei der Abg. Cornelia Julia Ecker.")
        self.assertEqual(results[0].description, "")
        self.assertEqual(results[0].quote, "")
        self.assertEqual(len(results[0].activityList), 1)
        self.assertEqual(results[0].activityList[0], "applause")        
        self.assertEqual(len(results[0].entityList), 3)
        self.assertEqual(results[0].entityList[0].type, expectedEntity1.type)
        self.assertEqual(results[0].entityList[0].name, expectedEntity1.name)
        self.assertEqual(results[0].entityList[1].type, expectedEntity2.type)
        self.assertEqual(results[0].entityList[1].name, expectedEntity2.name)
        self.assertEqual(results[0].entityList[2].type, expectedEntity3.type)
        self.assertEqual(results[0].entityList[2].name, expectedEntity3.name)
        
    def test_run_generalApplause_shouldReturnItem(self):
        # arrange
        expectedEntity1 = Entity("politicalParty", "övp")
        expectedEntity2 = Entity("politicalParty", "spö")
        expectedEntity3 = Entity("politicalParty", "fpö")
        expectedEntity4 = Entity("politicalParty", "grüne")
        expectedEntity5 = Entity("politicalParty", "neos")
        
        # execute
        results = self.fsm.run("Allgemeiner Beifall.")
        
        # assert
        self.assertEqual(len(results), 1)
        
        self.assertEqual(results[0].rawSourceText, "Allgemeiner Beifall.")
        self.assertEqual(results[0].description, "")
        self.assertEqual(results[0].quote, "")
        self.assertEqual(len(results[0].activityList), 1)
        self.assertEqual(results[0].activityList[0], "applause")        
        self.assertEqual(len(results[0].entityList), 5)
        self.assertEqual(results[0].entityList[0].type, expectedEntity1.type)
        self.assertEqual(results[0].entityList[0].name, expectedEntity1.name)
        self.assertEqual(results[0].entityList[1].type, expectedEntity2.type)
        self.assertEqual(results[0].entityList[1].name, expectedEntity2.name)
        self.assertEqual(results[0].entityList[2].type, expectedEntity3.type)
        self.assertEqual(results[0].entityList[2].name, expectedEntity3.name)        
        self.assertEqual(results[0].entityList[3].type, expectedEntity4.type)
        self.assertEqual(results[0].entityList[3].name, expectedEntity4.name)
        self.assertEqual(results[0].entityList[4].type, expectedEntity5.type)
        self.assertEqual(results[0].entityList[4].name, expectedEntity5.name)

# todo: write tests for every known activity
#todos:
#m.run("Abg. Meinl-Reisinger: Geh bitte, he! – Abg. Stögmüller schneuzt sich – Zwischenruf von Abg. Hafenecker – Abg. Blah – na sowas –: Für die Bevölkerung ist die Polizei zuständig, Herr Kollege! – Präsident Sobotka gibt das Glockenzeichen.")
# complex parsing multiple items
#m.run("Beifall und Heiterkeit bei der FPÖ, ÖVP sowie bei Abgeordneten der SPÖ, Neos und den Grünen, dem Abg. Brandstätter und der Abgeordneten Cornellia Ecker.")


if __name__ == '__main__':
    unittest.main()