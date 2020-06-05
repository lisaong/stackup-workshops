# tests for continuous integration of the model
import unittest
import pickle
import tensorflow as tf
from sklearn.metrics import mean_squared_error,  mean_absolute_error

# https://docs.python.org/3.7/library/unittest.html
class ModelTestcase(unittest.TestCase):
    def setUp(self):
        """Called before every test case."""
        with open('ci_artifacts.pkl', 'rb') as f:
            ci_artifacts = pickle.load(f)
            self.df_windowed = ci_artifacts['df_windowed']
            self.model_filename = ci_artifacts['model_filename']

    def tearDown(self):
        """Called after every test case."""
        pass # nothing to do right now

    def testModel(self):
        """Model test case."""
        y = self.df_windowed['t-3']
        X = self.df_windowed.drop(columns=['t-3'])

        model = tf.keras.models.load_model(self.model_filename)
        y_pred = model.predict(X)
        mse = mean_squared_error(y, y_pred)
        mae = mean_absolute_error(y, y_pred)

        print(f'Test Passed: MSE: {mse}, MAE: {mae}')

if __name__ == "__main__":
    # run all tests
    unittest.main()