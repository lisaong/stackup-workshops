// https://eloquentarduino.github.io/2020/01/easy-tinyml-on-esp32-and-arduino/
#include "EloquentTinyML.h"

// Copied to Documents/Arduino/libraries/mask_or_not
#include "mlp_full.h"

#define NUMBER_OF_INPUTS 900
#define NUMBER_OF_OUTPUTS 1

// in future projects you may need to tweak this value
// it's a trial and error process
#define TENSOR_ARENA_SIZE 2*1024

// https://github.com/eloquentarduino/EloquentTinyML/issues/3
Eloquent::TinyML::TfLite<NUMBER_OF_INPUTS, NUMBER_OF_OUTPUTS, TENSOR_ARENA_SIZE> ml((unsigned char*)model_data);

void setup() {
  Serial.begin(115200);
}

void loop() {
  float input[NUMBER_OF_INPUTS];
  for (int i=0; i<NUMBER_OF_INPUTS; i++) {
    input[i] = random(-127, 127)/127.0;
    Serial.print(input[i]);
    Serial.print(",");
  }

  Serial.println("predicting...");
  float predicted = ml.predict(input);
  Serial.print("predicted ");
  Serial.println(predicted);
  delay(1000);
}