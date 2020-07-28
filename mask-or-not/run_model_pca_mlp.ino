#include "EloquentTinyML.h"

// Schema: pca_{input_size}x{output_size}.h
#include "pca_400x7.h"
// Schema: model_name_{input_size}.h
#include "mlp_7.h"

// in future projects you may need to tweak this value
// it's a trial and error process
#define TENSOR_ARENA_SIZE 2*1024

Eloquent::TinyML::TfLite<NUMBER_OF_INPUTS, NUMBER_OF_OUTPUTS, TENSOR_ARENA_SIZE> ml;
Eloquent::ML::Port::PCA pca;

void setup() {
  Serial.begin(115200);
  ml.begin((unsigned char*)model_data);
}

void loop() {
  float input[PCA_INPUT_SIZE];
  float features[NUMBER_OF_INPUTS];

  for (int i=0; i<PCA_INPUT_SIZE; i++) {
    input[i] = random(-127, 127)/127.0;
    Serial.print(input[i]);
    Serial.print(",");
  }
  Serial.println("");

  Serial.println("transforming...");
  pca.transform(input, features);

  Serial.println("predicting...");
  float predicted = ml.predict(features);
  Serial.print("predicted: ");
  Serial.println(predicted);
  delay(1000);
}