void setup() {
  Serial.begin(115200);
  delay(1000); // give me time to bring up serial monitor
}

void loop() {
  // Joystick
  Serial.print(analogRead(26));
  Serial.print(",");
  Serial.println(analogRead(27));
  delay(200);
}
