import unittest
from dataScraper.Parser.InitStateMachine import initStateMachine
from dataScraper.Parser.InfoItem import InfoItem

class SpeechInfoParserTests(unittest.TestCase):

    def setUp(self):
        self.fsm = initStateMachine()

    def test_run_unknownTextGiven_returnsItemWithUnknownActivity(self):
        # arrange
        expectedRawSourceText = "Hallo, das ist ein unbekannter Text!"
        expectedActivityListItem = "unknown"
             
        # execute
        results = self.fsm.run("Hallo, das ist ein unbekannter Text!")
        
        # assert
        self.assertEqual(len(results), 1)
        result = results[0]
        self.assertEqual(result.rawSourceText, expectedRawSourceText)
        self.assertEqual(len(result.activityList), 1)
        self.assertEqual(result.activityList[0], expectedActivityListItem)
        self.assertEqual(len(result.entityList), 0)
        self.assertEqual(result.description, "")
        

if __name__ == '__main__':
    unittest.main()