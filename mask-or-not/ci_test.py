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
            self.inputs = ci_artifacts['inputs']
            self.target = ci_artifacts['target']
            self.preprocessors = ci_artifacts['preprocessors']
            self.baseline = ci_artifacts['baseline']
            self.mlp = ci_artifacts['mlp']
            self.cnn = ci_artifacts['cnn']

    def tearDown(self):
        """Called after every test case."""
        pass

    def _testSkLearnModel(self, model_spec):
        model = model_spec['model']
        X = self.inputs[model_spec['input']]
        for p in model_spec['preprocessors']:
          X = self.preprocessors[p].transform(X)
        y_pred = model.predict(X)
        print(model)
        print(classification_report(self.target['y'], y_pred))

    def _testTFModel(self, model_spec):
        model = tf.keras.models.load_model(model_spec['h5'])
        X = self.inputs[model_spec['input']]
        for p in model_spec['preprocessors']:
          X = self.preprocessors[p].transform(X)
        y_pred = model.predict(X) >= 0.5
        print(model.summary())
        print(classification_report(self.target['y'], y_pred))

    def testBaseline(self):
        print('Testing Baseline')
        self._testSkLearnModel(self.baseline)

    def testMLP(self):
        print('Testing MLP')
        self._testTFModel(self.mlp)

    def testCNN(self):
        print('Testing CNN')
        self._testTFModel(self.cnn)

    def testCNNTFLite(self):
        print('Testing TFLite Model')
        self._testTFLiteModel(self.cnn)

    def _testTFLiteModel(self, model_spec):
        y_pred = []

        # Load TFLite model and allocate tensors.
        interpreter = tf.lite.Interpreter(model_path=model_spec['tflite'])
        interpreter.allocate_tensors()

        # Get input and output tensors.
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        input_shape = input_details[0]['shape']

        # Test model on input data.
        # Loop through each row of test_data and perform inference
        model_input = self.inputs[model_spec['input']]
        for i in range(model_input.shape[0]):

            # add batch dimension
            input_data = np.expand_dims(model_input[i], axis=0).astype('float32')
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()

            # The function `get_tensor()` returns a copy of the tensor data.
            # Use `tensor()` in order to get a pointer to the tensor.
            output_data = interpreter.get_tensor(output_details[0]['index'])
            y_pred.append(output_data[0][0])

        print(classification_report(self.target['y'], np.array(y_pred) >= 0.5))        

if __name__ == '__main__':
    # run all tests
    unittest.main()