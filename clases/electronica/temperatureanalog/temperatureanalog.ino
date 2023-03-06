#define lr 22
#define lg 24
double toC(double  n){
    return (n*5*100)/1024;
  }
void setup() {
  // put your setup code here, to run once:
  pinMode(lr,OUTPUT);
  pinMode(lg,OUTPUT);
  Serial.begin(9600);
  digitalWrite(lr,LOW);
  digitalWrite(lg,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  auto val=toC(analogRead(A0));
  if(val<26){
    digitalWrite(lr,HIGH);
    digitalWrite(lg,LOW);
  }else{
    digitalWrite(lg,HIGH);
    digitalWrite(lr,LOW);
  }
  Serial.print("valor:");
  Serial.println(val);
  delay(500);  
}
