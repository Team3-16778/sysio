void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    
    if (command == "LED_ON") {
      // Do something (like digitalWrite(LED_BUILTIN, HIGH))
      Serial.println("ACK: LED turned on");
    } else {
      Serial.println("ERR: Unknown command");
    }
  }
}
