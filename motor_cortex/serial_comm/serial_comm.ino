//TODO:
//1: See if it works
//2: Replace the delays with millis
//3: Add pan servo control

String nom = "Motor Cortex";
String msg;

void setup() {
  Serial.begin(9600);
}

void loop() {
  readSerialPort();

  if (msg != "") {
    sendData();
  }
  delay(500);
}

void readSerialPort() {
  msg = "";
  if (Serial.available()) {
    delay(10);
    while (Serial.available() > 0) {
      msg += (char)Serial.read();
    }
    Serial.flush();
  }
}

void sendData() {
  //write data
//  Serial.print(nom);
//  Serial.print(" received : ");
  Serial.print("Response: ");
  Serial.print(msg);
}
