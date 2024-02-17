#include <CapacitiveSensor.h>
CapacitiveSensor touch = CapacitiveSensor(13, 12);  
int i = 0;
void setup() {
  Serial.begin(9600); // inizializzo il monitor seriale
}

void loop() {
  long sensorValue = touch.capacitiveSensor(50);    // effettuo 50 letture al secondo.
  if(sensorValue > 100){    // secondo i test, rapidi, effettuati sul sensore, se esso genera da 100 in su, siamo in fase di una leggera pressione.
    Serial.print("Click mouse");
    Serial.print(i);
    Serial.print("Valore: ");
    Serial.println(sensorValue);
    i ++;   // conto quante volte clicco il sensore
  }
  else{
    Serial.println("#");  // simbolo di mancanza del tocco
  }
  delay(100);   // fermo il flusso di esecuzione per 100ms
}
