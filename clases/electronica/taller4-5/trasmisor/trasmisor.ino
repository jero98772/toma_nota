//include libs
#include <Keypad.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
//defininir estados
#define E0 0
#define E1 1
#define E2 2
#define E3 3
#define E4 4
unsigned int NEXT = E0;
String state="";


#define R 25
#define G 24
#define B 23
//defines pines
//sensores bandas
#define S1 30
#define S2 31
#define S3 32
#define S4 33
int lastsensor=0;
int stop=0;

//motores bandas
#define left 22
#define rigth 23

byte const horario[4] = {0b1100, 0b0110, 0b0011, 0b1001};
byte const antih[4]  =  {0b1001, 0b0011, 0b0110, 0b1100};

//define keypad pins

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
byte rowPins[ROWS] = {2,3,4,5};     //connect to the row pinouts of the keypad
byte colPins[COLS] = {6,7,8}; //connect to the column pinouts of the keypad
char key ='0';

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );


//define display

LiquidCrystal_I2C lcd(0x27, 16, 4);  //
char cmsg = ' ';

void displaymystuff(int lastsensor,String &currentstate){
    lcd.setCursor(0, 0);
    lcd.print("Ultimo sensor:");
    lcd.setCursor(14, 0);
    char sensorstate[1];
    sprintf(sensorstate, "%d", lastsensor);
    lcd.print(sensorstate);
    lcd.setCursor(0, 2);
    lcd.print("Estado actual:");
    lcd.setCursor(0, 3);
    lcd.print(currentstate);
    
}
void displaymystuff(int lastsensor,String &currentstate,int segs){
    
    lcd.setCursor(0, 0);
    lcd.print("Ultimo sensor:");
    lcd.setCursor(14, 0);
    char sensorstate[1];
    sprintf(sensorstate, "%d", lastsensor);
    lcd.print(sensorstate);
    lcd.setCursor(0, 1);
    lcd.print("tiempo faltante:");
    lcd.setCursor(17,1);
    if(segs>=10){
      char segschar[2];
      sprintf(segschar, "%d", segs);
      lcd.print(segschar);
      }
    else{
       char segschar[1];
       sprintf(segschar, "%d", segs);
       lcd.print(segschar);
      }

    lcd.setCursor(0, 2);
    lcd.print("Estado actual:");
    lcd.setCursor(0, 3);
    lcd.print(currentstate);
    
}
int readsensors(int last){
  if (digitalRead(S1) == HIGH){
    last=1;
  }  
  else if (digitalRead(S2) == HIGH){
    last=2;
  }  
  else if (digitalRead(S3) == HIGH){
    last=3;
  }  
  else if (digitalRead(S4) == HIGH){
    last=4;
  }
  return last;
}
void go_to(int destiny,int segs){
  Serial.print("destiny");
  Serial.println(destiny);
   int lastsensor=readsensors(lastsensor);
    while (true){
      Serial.print("loop");
      lastsensor=readsensors(lastsensor);
      if(getvalidkey(key)=='*'){
        pause();  
      }
      if(lastsensor==destiny){
        Serial.println("out");
        return;
        break;
      }
      else if(lastsensor==-1){
      }
      //do not get out
      else if(1==lastsensor){
         state="Izquierda";
        digitalWrite(left,LOW);
        digitalWrite(rigth,HIGH);
        displaymystuff(lastsensor,state,segs);
     }
     else if(4==lastsensor){
        state="Derecha";
        digitalWrite(rigth,LOW);
        digitalWrite(left,HIGH);
        displaymystuff(lastsensor,state,segs);
      }
      else if(lastsensor<destiny){
        state="Izquierda     ";
        digitalWrite(left,LOW);
        digitalWrite(rigth,HIGH);
        displaymystuff(lastsensor,state,segs);
      }
      else if(lastsensor>destiny){
        state="Derecha      ";
        digitalWrite(rigth,LOW);
        digitalWrite(left,HIGH);
        displaymystuff(lastsensor,state,segs);
      }
    }

}
void go_to(int destiny){
  Serial.print("destiny");
  Serial.println(destiny);
   int lastsensor=readsensors(lastsensor);
    while (true){
      Serial.print("loop");
      lastsensor=readsensors(lastsensor);
      if(getvalidkey(key)=='*'){
        pause();  
      }
      if(lastsensor==destiny){
        return;
        break;
      }
      else if(lastsensor==-1){
      }
      //do not get out
      else if(1==lastsensor){
         state="Izquierda";
        digitalWrite(left,LOW);
        digitalWrite(rigth,HIGH);
        displaymystuff(lastsensor,state);
     }
     else if(4==lastsensor){
        state="Derecha";
        digitalWrite(rigth,LOW);
        digitalWrite(left,HIGH);
        displaymystuff(lastsensor,state);
      }
      else if(lastsensor<destiny){
        state="Izquierda     ";
        digitalWrite(left,LOW);
        digitalWrite(rigth,HIGH);
        displaymystuff(lastsensor,state);
      }
      else if(lastsensor>destiny){
        state="Derecha      ";
        digitalWrite(rigth,LOW);
        digitalWrite(left,HIGH);
        displaymystuff(lastsensor,state);
      }
    }

}
void offmotors(){
    digitalWrite(rigth,LOW);
    digitalWrite(left,LOW);
  }
void myoff(){
    state="Tarea finalizada";
    offmotors();
    displaymystuff(lastsensor,state);
  }
void mydelay(unsigned long interval){
      offmotors();
      delay(interval);
      
}
int countdown(int times,int lastsensor,int total){
    state="Detenido";
    Serial.println(times);
            for(int j=0;j<times;j++){
              lcd.clear();
              displaymystuff(lastsensor,state,total);
              mydelay(1000);
              total-=1;
              if(total<0 || total==16){
                Serial.println("finish total");
                myoff();
                return;
                break;

              }
            }
    Serial.println("count down?");
    return total;
}

void state1(){
  int total=5;
  for(int i=0;i<3;i++){
      go_to(2,total);  
      total--;
      go_to(3,total);
      total--;
  }
   myoff();
}
void state2(){
      //const unsigned long interval = 2000;
      int total=2*4;
      state="Detenido";
      int lastsensor=0;
      for(int i=0;i<2;i++){
            go_to(1,total);
            lastsensor=1;
            total=countdown(2,lastsensor,total);
            go_to(4,total);
            lastsensor=4;
            total=countdown(2,lastsensor,total);

            Serial.println("finish i");

      }
      Serial.println("im state4");
      myoff();
      return;
}
void state3(){
      //const unsigned long interval = 4000;
      int total=3*9;
      state="Detenido";
      int lastsensor=0;
      for(int i=0;i<4;i++){
            go_to(1,total);
            lastsensor=1;
            total=countdown(4,lastsensor,total);
            go_to(4,total);
            lastsensor=4;
            total=countdown(4,lastsensor,total);
            
      }
      myoff();
      return ;
}
 /*
void state1(){
      go_to(2);
      go_to(3);
      go_to(2);  
      go_to(3);
      go_to(2);  
      go_to(3);
      myoff();
      
}
void state2(){
      const unsigned long interval = 2000;
      int total=2*4;
      go_to(1,total);
      mydelay(interval);
      total-=2;
      go_to(4,total);
      mydelay(interval);
      total-=2;

      go_to(1,total);
      mydelay(interval);
      total-=2;
      go_to(4,total); 
      mydelay(interval);
      total-=2;
      displaymystuff(lastsensor,state,total);
      myoff();
      
}
void state3(){
      const unsigned long interval = 4000;
      int total=4*7;
      go_to(1,total);
      mydelay(interval);
      total-=4;
      go_to(4,total);
      mydelay(interval);
      total-=4;
      go_to(1,total);
      mydelay(interval);
      total-=4;
      go_to(4,total);
      mydelay(interval);
      total-=4;
      go_to(1,total);
      mydelay(interval);
      total-=4;
      go_to(4,total);
      mydelay(interval);
      total-=4;
      go_to(1,total);
      mydelay(interval);
      total-=4;
      go_to(4,total); 
      displaymystuff(lastsensor,state,total);
      myoff();
      
}
*/
char getvalidkey(char beforekey){
  char key = keypad.getKey();
  if(key!=' '){
    return key;
  }else{
    return beforekey;
  }
}
void pause(){//funciona
  offmotors();
  state="Detenieda      ";
  displaymystuff(lastsensor,state);
  while(true){//stop undefined
        key = getvalidkey(key);
        Serial.print(key);
        Serial.print("detenido *");
        if(key == '#'){
          state="Indefinido      ";
          key = getvalidkey(key);
          displaymystuff(lastsensor,state);
          Serial.print("yo no detenido #");
          break;
        }
   }
}
void setup() {
  pinMode(left, OUTPUT);     
  pinMode(rigth, OUTPUT);     
  pinMode(S1, INPUT);      
  pinMode(S2, INPUT);      
  pinMode(S3, INPUT);  
  pinMode(S4, INPUT);      
    
  lcd.init();
  //Encender la luz de fondo.
  lcd.backlight();
  //displaymystuff(0,state);
  Serial.begin(9600);
  Serial3.begin(9600);
}
void loop() {
  int lastsensor=readsensors(lastsensor);
  state="Disponible      ";
  key = getvalidkey(key);
  for(int i=0;i<100;i++){
  Serial3.println(key);
    
    }
  Serial.println(key);

  if (Serial3.available() > 0){
    char c = Serial3.read();
    Serial.println(c);
  if (c == 'l') {
    analogWrite(R, 255);
    analogWrite(G, 0);
    analogWrite(B, 0);
  } else if (c == 'r') {
    analogWrite(R, 0);
    analogWrite(G, 0);
    analogWrite(B, 255);
  } else if (c == 's') {
    analogWrite(R, 0);
    analogWrite(G, 255);
    analogWrite(B, 0);
  }      
  }   
}
