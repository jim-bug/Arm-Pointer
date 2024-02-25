#include <CapacitiveSensor.h>
CapacitiveSensor touch = CapacitiveSensor(9, 8);  
int i = 0;
void setup() {
  Serial.begin(9600); // inizializzo il monitor seriale
}

void loop() {
  long sensorValue = touch.capacitiveSensor(30);    // effettuo 50 letture al secondo.
  Serial.println(sensorValue);
  delay(100);   // fermo il flusso di esecuzione per 100ms
}
