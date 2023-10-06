/*.Controlar un motor paso a paso conectado a los cuatro bits menos significativos del PORTA, de tal manera
que si el suiche conectado a PINC,0 esta en uno gire a la derecha y si el suiche esta en cero, el motor gira a la izquierda.*/
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

int cont;
byte const horario[4] = {0b1100, 0b0110, 0b0011, 0b1001};
byte const antih[4]  =  {0b1001, 0b0011, 0b0110, 0b1100};
int pomodoros=0;
void setup()
{
  lcd.init();

  //Encender la luz de fondo.
  lcd.backlight();

  // Escribimos el Mensaje en el LCD.
  lcd.print("POMODOROS:");
  pinMode(22, OUTPUT);     //define pin 22 como salida
  pinMode(23, OUTPUT);     //define pin 23 como salida
  pinMode(24, OUTPUT);     //define pin 24 como salida
  pinMode(25, OUTPUT);     //define pin 25 como salida
}

void loop() {
    lcd.setCursor(0, 1);
    lcd.print(pomodoros);
    //delay(100);
    //lcd.print(" Valor");
    //lcd.setCursor(14, 1);
    //lcd.print(key);
    delay(100);
    cont = 0;                             // Se pone cont en cero
    while (cont < 4 ) // Mientras que cont sea menor a 4 y sw este encendido
    {
      PORTA = (horario[cont]);              // Envíe al PORTA la información de la tabla de horario
      delay(10);                             // Retardo de 100 milisegundos
      cont++;                               // Incremente la variable cont
    }
}


