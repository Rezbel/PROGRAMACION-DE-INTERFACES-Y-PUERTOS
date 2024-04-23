int potenciometro= A0;

void setup(){

}

int valorP;
void loop(){
  valorP = analogRead(potenciometro);
  Serial.print(valorP);
}