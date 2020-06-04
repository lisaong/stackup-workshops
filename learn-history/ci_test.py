# tests for continuous integration of the model
import unittest
import pandas as pd

# the test assumes Colab notebook downloaded this CSV file
# so we don't have to download again.
CSV_FILE = 'gross-domestic-product-in-chained-2015-dollars-year-on-year-growth-rate-quarterly.csv'

# https://docs.python.org/3.7/library/unittest.html
class ModelTestcase(unittest.TestCase):
    def setUp(self):
        """Called before every test case."""
        self.df = pd.read_csv(CSV_FILE)

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