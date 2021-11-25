#include <HCPCA9685.h>
#include <Wire.h>

#define  I2CAdd 0x40
HCPCA9685 HCPCA9685(I2CAdd);
int joyX = 0;
int joyY = 1;
int joyVal;
int joyValLeft;
int joyValRight;

void setup() {
  HCPCA9685.Init(SERVO_MODE);
  HCPCA9685.Sleep(false);
}

void loop() {
//  unsigned int Pos;/
  joyVal = analogRead(joyX);
  joyVal = map(joyVal, 0, 1023, 90, 350);
  HCPCA9685.Servo(2,joyVal);

  joyVal = analogRead(joyY);
  joyValLeft = map(joyVal, 0, 1023, 50, 350);
  joyValRight = map(joyVal, 0, 1023, 350, 50);
  HCPCA9685.Servo(0, joyValLeft);
  HCPCA9685.Servo(1, joyValRight);
  delay(50);
}
