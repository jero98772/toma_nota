
#define R 25
#define G 24
#define B 23

char c = ' ';


void setup() {
  // put your setup code here, to run once:
  Serial3.begin(9600);
  Serial.begin(9600);
  pinMode(R, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(B, OUTPUT);
}

void loop() {

  
  if (Serial3.available() > 0)
    c = Serial3.read();
    Serial.println(c);
  if (c == 'r') {
    analogWrite(R, 255);
    analogWrite(G, 0);
    analogWrite(B, 0);
  } else if (c == 'b') {
    analogWrite(R, 0);
    analogWrite(G, 0);
    analogWrite(B, 255);
  } else if (c == 'g') {
    analogWrite(R, 0);
    analogWrite(G, 255);
    analogWrite(B, 0);
  }
 

  // put your main code here, to run repeatedly:
}
