#include<TimerOne.h>
#define CP 7
#define EP 6
#define LM 5
#define ER 4
#define LI 20
#define EI 2
#define LA 8
#define EA 21
#define SU 14
#define EU 15
#define LB 16
#define LO 17


#define MULT 22
#define LDA 13
#define ADD 12
#define SUB 11

#define OUT 10
#define HLT 9
#define CLK 18
#define CLR 19
/*
CE ??
EE ??
*/
bool clkState = false;
int COUNTER=0;
bool running=true;
void setup() {
  // Configurar pines como entrada/salida según corresponda
  pinMode(CLK, OUTPUT);
  pinMode(CLR, OUTPUT);
  pinMode(LDA, INPUT);
  pinMode(ADD, INPUT);
  pinMode(SUB, INPUT);
  pinMode(OUT, INPUT);

  pinMode(CP, OUTPUT);
  pinMode(EP, OUTPUT);
  pinMode(LM, OUTPUT);
  pinMode(ER, OUTPUT);
  pinMode(LI, OUTPUT);
  pinMode(EI, OUTPUT);
  pinMode(LA, OUTPUT);
  pinMode(EA, OUTPUT);
  pinMode(SU, OUTPUT);
  pinMode(EU, OUTPUT);
  pinMode(LB, OUTPUT);
  pinMode(LO, OUTPUT);

  // Inicializar pines a un estado bajo
  digitalWrite(CLK, LOW);
  digitalWrite(CP, LOW);
  digitalWrite(EP, LOW);
  digitalWrite(LM, LOW);
  digitalWrite(ER, LOW);
  digitalWrite(LI, LOW);
  digitalWrite(EI, LOW);
  digitalWrite(LA, LOW);
  digitalWrite(EA, LOW);
  digitalWrite(SU, LOW);
  digitalWrite(EU, LOW);
  digitalWrite(LB, LOW);
  digitalWrite(LO, LOW);
}

void lda() {
  digitalWrite(EI, HIGH);
  digitalWrite(LM, HIGH);
  rSignal();
  digitalWrite(LM, LOW);
  digitalWrite(EI, LOW);
  digitalWrite(LA, HIGH);
  rSignal();
  digitalWrite(LA, LOW);
  COUNTER++;
  Serial.println("LDA Finish");

}

void add() {
  //Poner en el puerto el numero de la direccion de LDB
  digitalWrite(EI, HIGH);
  digitalWrite(LM, HIGH);
  rSignal();
  digitalWrite(LM, LOW);
  digitalWrite(EI, LOW);
  digitalWrite(LB, HIGH);
  rSignal();
  digitalWrite(LB, LOW);
  digitalWrite(ADD, HIGH);
  digitalWrite(ADD, LOW);
  digitalWrite(EU, HIGH);
  digitalWrite(LA, HIGH);
  rSignal();
  digitalWrite(LA, LOW);
  digitalWrite(EU, LOW);
  COUNTER++;
}


void sub() {
  digitalWrite(EI, HIGH);
  digitalWrite(LM, HIGH);
  rSignal();
  digitalWrite(LM, LOW);
  digitalWrite(EI, LOW);
  digitalWrite(LB, HIGH);
  rSignal();
  digitalWrite(LB, LOW);
  digitalWrite(SUB, HIGH);
  digitalWrite(SUB, LOW);
  digitalWrite(EU, HIGH);
  digitalWrite(LA, HIGH);
  rSignal();
  digitalWrite(LA, LOW);
  digitalWrite(EU, LOW);
  COUNTER++;

}
void mul() {
  digitalWrite(EI, HIGH);
  digitalWrite(LM, HIGH);
  rSignal();
  digitalWrite(LM, LOW);
  digitalWrite(EI, LOW);
  digitalWrite(LB, HIGH);
  rSignal();
  digitalWrite(LB, LOW);
  digitalWrite(MULT, HIGH);
  digitalWrite(MULT, LOW);
  digitalWrite(EU, HIGH);
  digitalWrite(LA, HIGH);
  rSignal();
  digitalWrite(LA, LOW);
  digitalWrite(EU, LOW);
  COUNTER++;
}

void call() {  
  digitalWrite(EI,HIGH);
  digitalWrite(LA,HIGH);
  rSignal();
  digitalWrite(LA, LOW);
  digitalWrite(EI, LOW);
  digitalWrite(EA,HIGH);
  digitalWrite(LI,HIGH);
  rSignal();
  digitalWrite(LI,LOW);
  digitalWrite(EA,LOW);
  COUNTER++;

}

void out() {
  digitalWrite(EA, HIGH);
  digitalWrite(LO, HIGH);
  rSignal();
  digitalWrite(LO, LOW);
  rSignal();
  digitalWrite(EA, LOW);
  COUNTER++;
}

void clockSignal() {
  clkState = !clkState;
  digitalWrite(CLK, clkState);
}

void rSignal() {
  while (digitalRead(CLK) == LOW) {
  }
  while (digitalRead(CLK) == HIGH) {
  }
}
void hlt() {
  while (true) {}
}
void loop() {
  Serial.print("PC: ");
  Serial.println(COUNTER);
  COUNTER++;
  digitalWrite(LM, HIGH);
  rSignal();
  digitalWrite(LM, LOW);
  digitalWrite(LI, HIGH);
  rSignal();
  digitalWrite(LI, LOW);
  Serial.print("PINA: ");
  Serial.println(COUNTER);
  switch (COUNTER) {
    case B00000001:
      Serial.println("LDA");
      lda();
      break;
    case B00000010:
      Serial.println("ADD");
      add();
      break;
    case B00000011:
      Serial.println("SUB");
      sub();
      break;
    case B00000101:
      Serial.println("MUL");
      mul();
      break;
    case B00000111:
      Serial.println("OUT");
      out();
      break;
    case B00001000:
      Serial.println("CALL");
      call();
      break;
    case B00001010:
      Serial.println("HLT");
      hlt();
      break;
  }
}
