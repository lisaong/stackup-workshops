# tests for continuous integration of the model
import unittest
import numpy as np
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
            self.tflite_filename = ci_artifacts['tflite_filename']
            self.h_filename = ci_artifacts['h_filename']

        X_scaled = self.X_scaler.transform(self.X)
        self.Z = self.X_pca.transform(X_scaled)

    def tearDown(self):
        """Called after every test case."""
        pass

    def testModel(self):
        """Model test case."""
        mlp = tf.keras.models.load_model(self.mlp_filename)
        y_pred_mlp = mlp.predict(self.Z) >= 0.5

        print(mlp.summary())
        print(classification_report(self.y, y_pred_mlp))

        y_pred_lr = self.lr.predict(self.Z)
        print(self.lr)
        print(classification_report(self.y, y_pred_lr))

        print(f'Test Passed')

    def testQuantizedModel(self):
        y_pred = []

        # Load TFLite model and allocate tensors.
        interpreter = tf.lite.Interpreter(model_path=self.tflite_filename)
        interpreter.allocate_tensors()

        # Get input and output tensors.
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        input_shape = input_details[0]['shape']

        # Test model on input data.
        # Loop through each row of test_data and perform inference
        for i in range(self.Z.shape[0]):

            # add batch dimension
            input_data = np.expand_dims(self.Z[i], axis=0).astype('float32')
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()

            # The function `get_tensor()` returns a copy of the tensor data.
            # Use `tensor()` in order to get a pointer to the tensor.
            output_data = interpreter.get_tensor(output_details[0]['index'])
            y_pred.append(output_data[0][0])

        print(classification_report(self.y, np.array(y_pred) >= 0.5))

    def testModelCodeFile(self):
        with open(self.h_filename, 'r') as f:
          print(f.read())

if __name__ == "__main__":
    # run all tests
    unittest.main()