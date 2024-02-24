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
        x += 10;
    }
    if (digitalRead(SW2)){
        y += 10;
    }
    Serial.println(x);
    Serial.println(y);
    Serial.println(digitalRead(SW3));
}