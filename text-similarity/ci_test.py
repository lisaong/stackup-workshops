# tests for continuous integration of the model
import unittest
import spacy

class ModelTestcase(unittest.TestCase):
    def setUp(self):
        """Called before every test case."""
        pass

    def tearDown(self):
        """Called after every test case."""
        pass

    def testModel(self):
        """Model test case."""
        nlp = spacy.load("en_core_web_md")
        tokens = nlp("hello world this is a test")
        assert len(tokens) > 0
        print(f'Test Passed: found {len(tokens)} tokens')

if __name__ == "__main__":
    # run all tests
    unittest.main()