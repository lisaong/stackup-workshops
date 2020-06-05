# tests for continuous integration of the model
import unittest
import pickle

# https://docs.python.org/3.7/library/unittest.html
class ModelTestcase(unittest.TestCase):
    def setUp(self):
        """Called before every test case."""
        with open('ci_artifacts.pkl', 'rb') as f:
            ci_artifacts = pickle.load(f)
            self.df = ci_artifacts['df']

    def tearDown(self):
        """Called after every test case."""
        pass # nothing to do right now

    def testModel(self):
        """Model test case."""
        assert self.df.shape[0] > 0
        print(f'Test Passed: dataset has {self.df.shape[0]} rows')

if __name__ == "__main__":
    # run all tests
    unittest.main()