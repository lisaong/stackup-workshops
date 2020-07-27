#include <BluetoothSerial.h>
#include "EloquentTinyML.h"

// Schema: model_name_{input_size}.h
#include "cnn_10.h"

// in future projects you may need to tweak this value
// it's a trial and error process
#define TENSOR_ARENA_SIZE 5*1024

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

// Globals
BluetoothSerial Bluetooth;
Eloquent::TinyML::TfLite<NUMBER_OF_INPUTS, NUMBER_OF_OUTPUTS, TENSOR_ARENA_SIZE> Model;

void logMemory() {
  // https://thingpulse.com/esp32-how-to-use-psram/
  // To see the log in Serial Monitor: Tools > Core Debug Level > Verbose
  log_d("Total heap: %d", ESP.getHeapSize());
  log_d("Free heap: %d", ESP.getFreeHeap());
}

void callback(esp_spp_cb_event_t event, esp_spp_cb_param_t *param){
  if(event == ESP_SPP_SRV_OPEN_EVT){
    Serial.println("Client Connected");
  }

  if(event == ESP_SPP_CLOSE_EVT ){
    Serial.println("Client disconnected");
  }
}

void onDataCallback(const uint8_t *buffer, size_t size) {
  Serial.printf("onDataCallback(%p, %d)", buffer, size);
  for (size_t i=0; i<size; i++) {
    Serial.printf("%d,", buffer[i]);
  }
}

void setup() {
  logMemory();

  Serial.begin(115200);

  Bluetooth.register_callback(callback);

  // For this to compile, you need the latest version of esp32-arduino
  // refer to README.md
  Bluetooth.onData(onDataCallback);

  if (!Bluetooth.begin("ESP32 Bluetooth")) {
    Serial.println("Could not start bluetooth");
  } else {
    Serial.println("Bluetooth started");
  }

  Model.begin((unsigned char*)model_data);

  logMemory();
}

void loop() {
  float input[NUMBER_OF_INPUTS];

  int i=0;
  while (Bluetooth.available() && i<NUMBER_OF_INPUTS) {
    int byte = Bluetooth.read();
    input[i] = (byte-127)/127.0;
    Serial.print(input[i]);
    Serial.print(",");
    i++;
  }

  if (i==NUMBER_OF_INPUTS) {
    Serial.println("predicting...");
    float predicted = Model.predict(input);
    Serial.print("predicted: ");
    Serial.println(predicted);
  }

  delay(250);
}