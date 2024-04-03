#define LED_PIN PC13

void setup() {
   pinMode(PA10, INPUT_PULLUP); // RX
   pinMode(PA9, OUTPUT); // TX

   Serial1.begin(9600);
   Serial.begin(9600);

   pinMode(LED_PIN, OUTPUT); // Se configura el pin PC13 como salida
}

void loop() {

    digitalWrite(LED_PIN, HIGH);


   if (Serial1.available()) {
      char c = Serial1.read();
      Serial.write(c);
   }

   if (Serial.available()) {
      char c = Serial.read();
      Serial1.write(c);
   }

   // Verificar si hay una conexión entrante al módulo HC-06
   if (Serial1.peek() == ':') {
      digitalWrite(LED_PIN, LOW); // Encender el LED en el pin PC13
      delay(500);
      digitalWrite(LED_PIN, HIGH);
   } else {
      digitalWrite(LED_PIN, HIGH); // Apagar el LED en el pin PC13
      delay(500);
   }
   delay(500);
}
