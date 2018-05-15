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
#include "classifier_16k.i.h"
%}

#if defined(SWIGPYTHON)
%pythoncode %{

def predict(inputData: 'numpy.ndarray') -> "numpy.ndarray":
    """Convenience function for calling the model with NumPy arrays"""
    import numpy as np
    results = FloatVector(get_default_output_shape().Size())
    model_Predict(None, inputData, results)
    return np.asarray(results)


%}
#endif // defined(SWIGPYTHON)

%include "classifier_16k.i.h"
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

