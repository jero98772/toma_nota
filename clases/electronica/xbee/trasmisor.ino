 

#define POT 0

char c = ' ';


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //Usaremos el Tx3
  Serial3.begin(9600);
  pinMode(POT, INPUT);

}

void loop() {

  int valor = analogRead(A0);
  valor = map(valor, 0,1023,0,100);
  Serial.println(valor);
  if (valor > 0 && valor < 30)
  {
    Serial3.println('r');
    Serial.println('r');
  }
  else if (valor >= 30 && valor < 70)
  {
    Serial3.println('b');
    Serial.println('b');
  }
    else if (valor >= 70 && valor <= 100)
  {
    Serial3.println('g');
    Serial.println('g');
  }


  // put your main code here, to run repeatedly:
}

