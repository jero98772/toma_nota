/*.Controlar un motor paso a paso conectado a los cuatro bits menos significativos del PORTA, de tal manera
que si el suiche conectado a PINC,0 esta en uno gire a la derecha y si el suiche esta en cero, el motor gira a la izquierda.*/

int cont;
const int sw = 37;     //define sw para el pin 37
byte const horario[4] = {0b1100, 0b0110, 0b0011, 0b1001};
byte const antih[4]  =  {0b1001, 0b0011, 0b0110, 0b1100};

void setup()
{
  pinMode(22, OUTPUT);     //define pin 22 como salida
  pinMode(23, OUTPUT);     //define pin 23 como salida
  pinMode(24, OUTPUT);     //define pin 24 como salida
  pinMode(25, OUTPUT);     //define pin 25 como salida
  pinMode(sw, INPUT);      //define sw como entrada
}

void loop() {

  if (digitalRead(sw) == HIGH) // Pregunta si SW esta encendido
  {
    cont = 0;                             // Se pone cont en cero
    while (cont < 4 && digitalRead(sw) == HIGH) // Mientras que cont sea menor a 4 y sw este encendido
    {
      PORTA = (horario[cont]);              // Envíe al PORTA la información de la tabla de horario
      delay(10);                             // Retardo de 100 milisegundos
      cont++;                               // Incremente la variable cont
    }
  }
  else                                     // de lo contrario
  {
    cont = 0;                             // la variable cont=0
    while (cont < 4 && digitalRead(sw) == LOW) // Mientras que cont sea menor a 4 y sw este apagado
    {
      PORTA = (antih[cont]);                // Envíe al PORTA la información de la tabla de antih
      delay(10);                             // Retardo de 100 milisegundos
      cont++;                               // Incremente la variable cont
    }
  }
}


