#include "EloquentTinyML.h"

// Schema: model_name_{input_size}.h
#include "cnn_10.h"

// in future projects you may need to tweak this value
// it's a trial and error process
#define TENSOR_ARENA_SIZE 2*1024

Eloquent::TinyML::TfLite<NUMBER_OF_INPUTS, NUMBER_OF_OUTPUTS, TENSOR_ARENA_SIZE> ml;

void setup() {
  Serial.begin(115200);
  ml.begin((unsigned char*)model_data);
}

void loop() {
  float input[NUMBER_OF_INPUTS];

  for (int i=0; i<NUMBER_OF_INPUTS; i++) {
    input[i] = random(-127, 127)/127.0;
    Serial.print(input[i]);
    Serial.print(",");
  }
  Serial.println("");

  Serial.println("predicting...");
  float predicted = ml.predict(input);
  Serial.print("predicted: ");
  Serial.println(predicted);
  delay(1000);
}