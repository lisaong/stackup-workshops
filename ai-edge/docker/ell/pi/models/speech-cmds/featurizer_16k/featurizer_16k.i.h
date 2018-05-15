//
// ELL SWIG header for module mfcc
//

#pragma once

#if !defined(SWIG)
//
// ELL header for module mfcc
//

#include <stdint.h>

#if defined(__cplusplus)
extern "C"
{
#endif // defined(__cplusplus)

//
// Types
//

#if !defined(ELL_TensorShape)
#define ELL_TensorShape

typedef struct TensorShape
{
    int32_t rows;
    int32_t columns;
    int32_t channels;
} TensorShape;

#endif // !defined(ELL_TensorShape)

//
// Functions
//

// Input size: 160
// Output size: 40
void mfcc_Predict(void* context, float* input0, float* output0);

int32_t mfcc_GetInputSize();

int32_t mfcc_GetOutputSize();

int32_t mfcc_GetNumNodes();

void mfcc_GetInputShape(int32_t index, TensorShape* shape);

void mfcc_GetOutputShape(int32_t index, TensorShape* shape);

#if defined(__cplusplus)
} // extern "C"
#endif // defined(__cplusplus)

#endif // !defined(SWIG)

void mfcc_Predict(void* context, const std::vector<float>& input, std::vector<float>& output);

#if !defined(SWIG)
void mfcc_Predict(void* context, const std::vector<float>& input, std::vector<float>& output)
{
    mfcc_Predict(context, const_cast<float*>(&input[0]), &output[0]);
}
#endif // !defined(SWIG)

