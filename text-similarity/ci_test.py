# tests for continuous integration of the model
import unittest
import pickle

class ModelTestcase(unittest.TestCase):
    def setUp(self):
        """Called before every test case."""
        ci_artifacts = pickle.load(open('ci_artifacts.pkl', 'rb'))

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