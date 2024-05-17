int ENA = 4;
int IN1 = 5;
int IN2 = 6;
int PIR = 7;
int LDR = A0;
int relevador = 13;

void setup() {
  // Inicializar comunicación serial
  Serial.begin(9600);
  Serial.setTimeout(10);
  
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(relevador, OUTPUT);
  pinMode(PIR, INPUT_PULLUP);
}

void loop() {
  int valPIR = digitalRead(PIR); 
  
  if(valPIR == HIGH){
    int v = millis() % 3; 
    if (v == 0) {
      Serial.println("Detenerse");
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      analogWrite(ENA, 0);
    } else if (v == 1) {
      Serial.println("Girar Izquierda");
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      analogWrite(ENA, 255);
    } else if (v == 2) {
      Serial.println("Girar Derecha");
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      analogWrite(ENA, 255);
    }
  }

  int valLDR = analogRead(LDR);

  if(valLDR > 500){
    digitalWrite(relevador, HIGH);
    Serial.print("Estado Aplicado: ");
    Serial.println(valLDR);
  } else {
    digitalWrite(relevador, LOW);
  }

  delay(2000); 
}
