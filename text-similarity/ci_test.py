# tests for continuous integration of the model
import unittest
import spacy
import pickle

class ModelTestcase(unittest.TestCase):
    def __init__(self):
        """Constructor (do expensive initialisation here)."""
        self.nlp = spacy.load("en_core_web_md")
        self.ci_artifacts = pickle.load(open('ci_artifacts.pkl', 'rb'))

    def setUp(self):
        """Called before every test case."""
        self.text_clean = ci_artifacts['text_clean']
        self.text_vectors_clean = ci_artifacts['text_vectors_clean']

    def tearDown(self):
        """Called after every test case."""
        pass

    def testModel(self):
        """Model test case."""
        print(self.text_clean)
        assert self.text_vectors_clean.shape[1] == 300
        print(f'Test Passed: loaded vectors of shape: {self.text_vectors_clean.shape}')

if __name__ == "__main__":
    # run all tests
    unittest.main()