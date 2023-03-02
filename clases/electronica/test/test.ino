int pin=13;
int r=22;
int g=23;
int b=24;
int s=0;
int pot1=A7;
int pot2=A6;
void setup() {
  Serial.begin(115200);
  pinMode(r,OUTPUT);
  pinMode(g,OUTPUT);
  pinMode(b,OUTPUT);
}

void loop() {
int pot1v=analogRead(pot1);
int pot2v=analogRead(pot1);

Serial.println(pot2v);
for(int i=22;i<37;i++){

for(int i=22;i<37;i++){
  pot1v=analogRead(pot1);
  pot2v=analogRead(pot2);
  Serial.println(pot1v);

    delay(1*pot1v);
    digitalWrite(i-1,LOW);
    digitalWrite(i,HIGH);
  analogWrite(g,pot1v); 
analogWrite(b,pot2v);

  }
}

digitalWrite(pin,LOW);
s++;
Serial.println(s);
}