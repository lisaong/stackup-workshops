//
// ELL SWIG interface for module model
//

%module(directors="1") model
%feature("autodoc", "3");

%include "callback.i"

// Propagate python callback exceptions
%feature("director:except") {
    if ($error != NULL) {
        PyObject* ptype = nullptr;
        PyObject* pvalue = nullptr;
        PyObject* ptraceback = nullptr;
        PyErr_Fetch(&ptype, &pvalue, &ptraceback);
        PyErr_Restore(ptype, pvalue, ptraceback);
        PyErr_Print();
        Py_Exit(1);
    }
}

%{
#include "model.i.h"
%}

WRAP_CALLABLES_AS_CALLBACKS(model_Predictor, FloatCallbackBase, float, FloatCallbackBase, float, DoubleCallbackBase)

%pythoncode %{
class Model:
    """Base class that user code derives from to provide callbacks"""
    def __init__(self):
        
        self.predictor = model_Predictor()

        # keep these wrapper objects alive so the model_Predictor C++ code can keep a pointer to them.
        self.input_wrapper = InputCallableWrapper(self._input_callback)
        self.output_wrapper = OutputCallableWrapper(self.output_callback)
        self.lag_wrapper = LagCallableWrapper(self.lag_notification)

        self.predictor.Register(self.input_wrapper,
          get_default_input_shape().Size(),
          self.output_wrapper,
          get_default_output_shape().Size(),
          self.lag_wrapper)

        self.input = FloatVector(get_default_input_shape().Size())
        self.result = FloatVector(get_default_output_shape().Size())

    def _input_callback(self, data: 'FloatVector') -> "bool":
        import numpy as np
        data.copy_from(self.input_callback().astype(np.float32).ravel())
        return True

    def input_callback(self) -> "numpy.ndarray":
        """Derived classes override this to return data as a Numpy array"""
        return None

    def output_callback(self, output: 'FloatVector'):
        """Derived classes override this to receive data as a FloatVector"""
        pass

    def lag_notification(self, lag):
        """Derived classes override this"""
        pass

    def get_step_interval(self) -> "double":
        """Returns the step interval in milliseconds"""
        return model_GetStepInterval()

    def get_lag_threshold(self) -> "double":
        """Returns the lag threshold in milliseconds"""
        return model_GetLagThreshold()

    def time_to_next_interval(self, current_time=0) -> "double":
        """Returns the time to next interval in milliseconds"""
        return model_GetTicksUntilNextInterval(current_time)

    def predict(self, current_time=0):
        """Runs predict with the current time in milliseconds"""
        model_Predict(self.predictor, current_time, self.result)


def predict(inputData: 'numpy.ndarray') -> "numpy.ndarray":
    """Convenience function for calling the model directly without callbacks"""

    class PredictWrapper(Model):
        "Internal class that feeds inputData and receives the result"
        
        def __init__(self, inputData):
            Model.__init__(self)
            self.input = inputData
            self.results = None

        def input_callback(self) -> "numpy.ndarray":
            "Callback when input is needed"
            return self.input

        def output_callback(self, output: 'FloatVector'):
            "Callback when output is available"
            import numpy as np
            self.results = np.asarray(output)

        def get_results(self) -> "numpy.ndarray":
            "Returns the cached results"
            return self.results

    wrapper = PredictWrapper(inputData)
    wrapper.predict()
    return wrapper.get_results()


%}
%include "model.i.h"
%include "shape.i";
%inline %{
  ell::api::math::TensorShape get_default_input_shape() {
    TensorShape  s;
    model_GetInputShape(0, &s);
    return ell::api::math::TensorShape{ s.rows, s.columns, s.channels };
  }
  ell::api::math::TensorShape get_default_output_shape() {
    TensorShape  s;
    model_GetOutputShape(0, &s);
    return ell::api::math::TensorShape{ s.rows, s.columns, s.channels };
  }
%}

