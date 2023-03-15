#define pin 2
void setup() {
  // put your setup code here, to run once:
  pinMode(pin,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=1000;i>0;i=i/1.11){
    delay(i);
    digitalWrite(pin,HIGH);
    delay(i);
    digitalWrite(pin,LOW);
    Serial.println(i);
  }
  
}
