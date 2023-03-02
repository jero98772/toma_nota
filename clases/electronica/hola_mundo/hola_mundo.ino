#include <Arduino.h>
int PIN=13;
void setup() {
  pinMode(PIN,OUTPUT);
}

void loop() {
  digitalWrite(PIN,HIGH);
  delay(50);
  digitalWrite(PIN,LOW);
  delay(50);
}
