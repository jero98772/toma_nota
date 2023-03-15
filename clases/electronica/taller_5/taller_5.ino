//https://www.tinkercad.com/things/aULpNGREqiF
//i use that pines because i need send analog values with pwd
#define red 11
#define green 6
#define blue 10
#define temp A0
double toC(double  n){
    return (((n*5)/1024)-0.5)*100;//max value is 358 on temperature sensor
  }
void setup(){
  Serial.begin(9600);
  pinMode(red,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop(){
  auto temperature=toC(analogRead(temp));
  Serial.println(temperature);
  if(temperature<=28){
  	analogWrite(red,255);
    analogWrite(green,201);
    analogWrite(blue,14);
  }else if(temperature>30 && temperature<=32){
   	analogWrite(red,255);
    analogWrite(green,128);
        analogWrite(blue,0);

  }else if(temperature>32){
    analogWrite(red,255);
        analogWrite(green,0);
    analogWrite(blue,0);
  }
}