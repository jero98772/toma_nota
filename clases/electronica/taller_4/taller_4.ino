// C++ code
//https://www.tinkercad.com/things/4rQoQhUHSiU
#define start 1
#define stop 2
#define snl 3
#define snh 4
#define evl 5
#define bh 6
#define agitador 7
void setup(){
  Serial.begin(9600);
  pinMode(start, INPUT);
  pinMode(snh, INPUT);
  pinMode(stop, INPUT);

  pinMode(evl, OUTPUT);
  pinMode(bh, OUTPUT);
  pinMode(agitador, OUTPUT);
}

void loop(){
  Serial.println();
  int startVal=digitalRead(start);
  int stopVal=digitalRead(stop);
  int snhVal=digitalRead(snh);
  if(stopVal==0){
      Serial.println("stop swich is activate");
  }
  //Serial.println("start swich is activate");
  //se hace un pull down
  Serial.println(startVal);
  if(startVal==0){
    Serial.println("start swich is activate");
    digitalWrite(bh,HIGH);
    if(snhVal==0){
        Serial.println("start snh is activate");
      	 delay(10000);
      	 for(int i=0;i<5;i++){
	      digitalWrite(agitador,HIGH);
          delay(30000);
          digitalWrite(agitador,LOW);
          delay(10000);
          Serial.print("Etapa ");
          Serial.print(i);
          Serial.println(" de 5");

      }
      
      digitalWrite(evl,HIGH);

    }
  }
  delay(500);
}