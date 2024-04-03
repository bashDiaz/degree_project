#define MOTOR_PIN PA0
#define LED_PIN PC13

void setup() {

pinMode(MOTOR_PIN, OUTPUT);
pinMode(LED_PIN, OUTPUT);

}

void loop() {
 digitalWrite(MOTOR_PIN, HIGH);
 digitalWrite(LED_PIN, LOW);
 delay(1000);
 digitalWrite(LED_PIN, HIGH);
 delay(1000);
}


