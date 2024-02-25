#include <CapacitiveSensor.h>
#define SW1 10
#define SW2 11
#define SW3 12
#define TS1_1 9     // Touch Sensor
#define TS1_2 8
#define TS2_1 7
#define TS2_2 6

struct click{
  bool stato;
  int count;
  // CapacitiveSensor touch;
};

click left;
click right;
CapacitiveSensor touchLeft = CapacitiveSensor(TS1_1, TS1_2);    
CapacitiveSensor touchRight = CapacitiveSensor(TS2_1, TS2_2);
int x = 0;
int y = 0;

void setup(){
    Serial.begin(9600);
    pinMode(SW1, INPUT);
    pinMode(SW2, INPUT);
    pinMode(SW3, INPUT);
}



void loop(){
    int sw1 = digitalRead(SW1);   // lettura stato pulsante che incrementa le ascisse
    int sw2 = digitalRead(SW2);   // lettura stato pulsante che incrementa le ordinate
    long leftClickValue = touchLeft.capacitiveSensor(50);   // effettuo 50 letture al secondo del sensore del click sinistro
    long rightClickValue = touchRight.capacitiveSensor(50); // effettuo 50 letture al secondo del sensore del click destro

    if (sw1 == 1){
        x += 10;
    }

    if (sw2 == 1){
        y += 10;
    }

    if(leftClickValue > 1000){      // se il valore dei sensori è > 1000 significa che il sensore è premuto
        left.stato = true;
        left.count ++;
        if(left.count > 2){
          left.count = 0;
        }
    }
    else{
        left.stato = false;
    }

    if(rightClickValue > 1000){
        right.stato = true;
        if(right.count > 2){
          right.count = 0;
        }
    }
    else{
        right.stato = false;
    }

    // invio i dati alla seriale a cui è collegato arduino.
    Serial.print(x);
    Serial.print(" ");
    Serial.print(y);
    Serial.print(" ");
    Serial.print(left.stato);
    Serial.print(" ");
    Serial.print(right.stato);
    Serial.print(" ");
    Serial.print(left.count);
    Serial.print("\n");
    delay(100);
}