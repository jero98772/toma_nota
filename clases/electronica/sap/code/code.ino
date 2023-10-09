#include<TimerOne.h>
#define Cp 7
#define Ep 6
#define Lm 5
#define Er 4
#define Li 20
#define Ei 2
#define La 8
#define Ea 21
#define Su 14
#define Eu 15
#define Lb 16
#define Lo 17


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

int COUNTER=0;
void setup() {
  // Configurar pines como entrada/salida según corresponda
  pinMode(CLK, OUTPUT);
  pinMode(CLR, OUTPUT);
  pinMode(LDA, INPUT);
  pinMode(ADD, INPUT);
  pinMode(SUB, INPUT);
  pinMode(OUT, INPUT);

  pinMode(Cp, OUTPUT);
  pinMode(Ep, OUTPUT);
  pinMode(Lm, OUTPUT);
  pinMode(Er, OUTPUT);
  pinMode(Li, OUTPUT);
  pinMode(Ei, OUTPUT);
  pinMode(La, OUTPUT);
  pinMode(Ea, OUTPUT);
  pinMode(Su, OUTPUT);
  pinMode(Eu, OUTPUT);
  pinMode(Lb, OUTPUT);
  pinMode(Lo, OUTPUT);

  // Inicializar pines a un estado bajo
  digitalWrite(CLK, LOW);
  digitalWrite(Cp, LOW);
  digitalWrite(Ep, LOW);
  digitalWrite(Lm, LOW);
  digitalWrite(Er, LOW);
  digitalWrite(Li, LOW);
  digitalWrite(Ei, LOW);
  digitalWrite(La, LOW);
  digitalWrite(Ea, LOW);
  digitalWrite(Su, LOW);
  digitalWrite(Eu, LOW);
  digitalWrite(Lb, LOW);
  digitalWrite(Lo, LOW);


void lda() {
  digitalWrite(Ei, HIGH);
  digitalWrite(Lm, HIGH);
  rSignal();
  digitalWrite(Lm, LOW);
  digitalWrite(Ei, LOW);
  digitalWrite(Ce, HIGH);
  digitalWrite(Ee, HIGH);
  digitalWrite(La, HIGH);
  rSignal();
  digitalWrite(LA, LOW);
  digitalWrite(CE, LOW);
  digitalWrite(, LOW);
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
  digitalWrite(CE, HIGH);
  digitalWrite(, HIGH);
  digitalWrite(LB, HIGH);
  rSignal();
  digitalWrite(LB, LOW);
  digitalWrite(CE, LOW);
  digitalWrite(, LOW);
  digitalWrite(ADD, HIGH);
  digitalWrite(ADD, LOW);
  digitalWrite(EU, HIGH);
  digitalWrite(LA, HIGH);
  rSignal();
  digitalWrite(LA, LOW);
  digitalWrite(EU, LOW);
  //PC++;
}

void mul() {
  digitalWrite(Ei, HIGH);
  digitalWrite(LM, HIGH);
  rSignal();
  digitalWrite(LM, LOW);
  digitalWrite(EI, LOW);
  digitalWrite(LB, HIGH);
  digitalWrite(CE, HIGH);
  digitalWrite(EE, HIGH);
  rSignal();
  digitalWrite(LB, LOW);
  digitalWrite(CE, LOW);
  digitalWrite(EE, LOW);
  digitalWrite(MUL, HIGH);
  digitalWrite(MUL, LOW);
  digitalWrite(EU, HIGH);
  digitalWrite(LA, HIGH);
  rSignal();
  digitalWrite(LA, LOW);
  digitalWrite(EU, LOW);
  //PC++;
}

void loop() {
  // Ciclo principal del SAP
  if (running) {
    // Ciclo de reloj del SAP
    digitalWrite(CLK, clockState);
    delay(100); // Ajusta la velocidad del reloj según sea necesario
    clockState = !clockState;

    if (clockState == LOW) {
      // En el flanco descendente del reloj, realiza las operaciones necesarias
      // Aquí puedes implementar las funciones del SAP como cargar, sumar, restar, mover datos, etc.
      if (digitalRead(LDA) == HIGH) {
        // Cargar datos en el acumulador desde la memoria
        bus = memory[registerA];
        accumulator = bus;
      }
      // Implementa otras funciones aquí

      if (digitalRead(HLT) == HIGH) {
        // Detener la ejecución si la señal HLT está activada
        running = false;
      }
    }
  }
}
