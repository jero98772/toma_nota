int pin=13;
int s=0;
void setup() {
  Serial.begin(115200);
  pinMode(pin,OUTPUT);
}

void loop() {
delay(1000);
digitalWrite(pin,HIGH);
delay(1000);
digitalWrite(pin,LOW);
s++;
Serial.println(s);
}
