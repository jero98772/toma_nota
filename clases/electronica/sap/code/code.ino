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

bool clockState = LOW;
bool running = true;
byte accumulator = 0;
byte registerA = 0;
byte bus = 0;
byte memory[256]; // Memoria del SAP

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
  
  // Inicializar la memoria del SAP con datos de prueba
  for (int i = 0; i < 256; i++) {
    memory[i] = i;
  }
  
  digitalWrite(CLR, HIGH);
  delay(1);
  digitalWrite(CLR, LOW);
  delay(10);
}

void lda() {
  // Instrucción LDA: Cargar datos en el acumulador desde la memoria
  bus = memory[registerA];
  accumulator = bus;
}

void add() {
  // Instrucción ADD: Sumar el valor en la memoria al acumulador
  bus = memory[registerA];
  accumulator += bus;
}

void mul() {
  // Instrucción MUL: Multiplicar el valor en la memoria por el acumulador
  bus = memory[registerA];
  accumulator *= bus;
}

void call(int address) {
  // Instrucción CALL (equivalente a GO TO): Cambiar la dirección de ejecución
  registerA = address;
}

void sub() {
  // Instrucción SUB: Restar el valor en la memoria al acumulador
  bus = memory[registerA];
  accumulator -= bus;
}

void out() {
  // Instrucción OUT: Enviar el valor del acumulador a la salida (por ejemplo, un LED)
  digitalWrite(OUT, accumulator);
}

void hlt() {
  // Instrucción HLT: Detener la ejecución del programa
  running = false;
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
