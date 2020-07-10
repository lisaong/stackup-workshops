# tests for continuous integration of the model
import unittest
import pickle
import tensorflow as tf
from sklearn.metrics import classification_report

class ModelTestcase(unittest.TestCase):
    def setUp(self):
        """Called before every test case."""
        with open('ci_artifacts.pkl', 'rb') as f:
            ci_artifacts = pickle.load(f)
            self.X = ci_artifacts['X']
            self.X_scaler = ci_artifacts['X_scaler']
            self.X_pca = ci_artifacts['X_pca']
            self.y = ci_artifacts['y']
            self.y_encoder = ci_artifacts['y_encoder']
            self.lr = ci_artifacts['lr']
            self.mlp_filename = ci_artifacts['mlp_filename']

    def tearDown(self):
        """Called after every test case."""
        pass

    def testModel(self):
        """Model test case."""
        X_scaled = self.X_scaler.transform(self.X)
        mlp = tf.keras.models.load_model(self.mlp_filename)
        y_pred_mlp = mlp.predict(X_scaled) >= 0.5

        print(mlp.summary())
        print(classification_report(y, y_pred_mlp))

        X_pca = self.X_pca.transform(X_scaled)
        y_pred_lr = self.lr.predict(X_pca)
        print(self.lr)
        print(classification_report(y, y_pred_lr))

        print(f'Test Passed')

if __name__ == "__main__":
    # run all tests
    unittest.main()