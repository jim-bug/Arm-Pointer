#define SW1 10
#define SW2 11
#define SW3 12

int x = 0;
int y = 0;
void setup(){
    Serial.begin(9600);
    pinMode(SW1, INPUT);
    pinMode(SW2, INPUT);
    pinMode(SW3, INPUT);
}
void loop(){
    if (digitalRead(SW1)){
        delay(50);
        x += 100;
        
    }
    if (digitalRead(SW2)){
        delay(50);
        y += 100;
    }
    Serial.print(x);
    Serial.print(" ");
    Serial.print(y);
    Serial.print(" ");
    Serial.print(digitalRead(SW3));
    Serial.print("\n");
    delay(20);
}