#include <Servo.h>

const int pinServo = 9; 
const int PIR = 2;
Servo servo;
int val = 0; 

void setup() {
  Serial.begin(9600); 
  servo.attach(pinServo); 
  pinMode(PIR, INPUT); 
}

void loop() {
  val = digitalRead(PIR); 
  if (val == HIGH) {
    servo.write(90);
    Serial.println("Movimiento Detectado... Moviendo Servo");
    delay(2000);
    servo.write(0);
    Serial.println("Esperando Movimiento...");
  }
  delay(1000);
}
