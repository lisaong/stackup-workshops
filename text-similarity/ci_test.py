# tests for continuous integration of the model
import unittest
import pickle
import spacy
from analysers import  KDramaSynopsisAnalyser

class ModelTestcase(unittest.TestCase):
    def setUp(self):
        """Called before every test case."""
        with open('ci_artifacts.pkl', 'rb') as f:
            ci_artifacts = pickle.load(f)
            self.text_original = ci_artifacts['text_original']
            self.text_clean = ci_artifacts['text_clean']
            self.text_vectors_clean = ci_artifacts['text_vectors_clean']
            self.sample_scores = ci_artifacts['sample_scores']

    def tearDown(self):
        """Called after every test case."""
        pass

    def testModel(self):
        """Model test case."""
        assert len(self.text_original) > len(self.text_clean)
        assert self.text_vectors_clean.shape[1] == 300
        assert self.text_vectors_clean.shape[0] == 50 # truncated
        assert len(self.sample_scores) == 3
        print(self.sample_scores)
        print(f'Test Passed')

if __name__ == "__main__":
    # run all tests
    unittest.main()