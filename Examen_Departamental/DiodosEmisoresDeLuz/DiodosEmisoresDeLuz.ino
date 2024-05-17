int LDR = A0;
int LED = 2;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(LED, OUTPUT);
}
int val;
void loop() {
  val = analogRead(LDR);
  if (val > 500) {
    digitalWrite(LED, 1);
    Serial.println("diodo prendido");
  } else {
    digitalWrite(LED, 0);
    Serial.println("Diodo apagado");
  }
  delay(100);
}
