#include <HCPCA9685.h>
#include <Wire.h>

#define  I2CAdd 0x40
HCPCA9685 HCPCA9685(I2CAdd);

const int status_red = 2;
const int status_green = 3;
const int status_blue = 4;

int joyX = 0;
int joyY = 1;

int pan;
int tilt;
int tiltLeft;
int tiltRight;

int panPrev;
int tiltLeftPrev;
int tiltRightPrev;

int smoothedPan;
int smoothedTilt;
int smoothedTiltLeft;
int smoothedTiltRight;

void setup() {
  HCPCA9685.Init(SERVO_MODE);
  HCPCA9685.Sleep(false);
  pan = analogRead(joyX);
  pan = map(pan, 0, 1023, 90, 400);
  tilt = analogRead(joyY);
  tiltLeft = map(tilt, 0, 1023, 50, 350);
  tiltRight = map(tilt, 0, 1023, 350, 50);
  HCPCA9685.Servo(0, tiltLeft);
  HCPCA9685.Servo(1, tiltRight);
  HCPCA9685.Servo(2, pan);
  panPrev = pan;
  tiltLeftPrev = tiltLeft;
  tiltRightPrev = tiltRight;
  
  int status_brightness = 0;
  while (status_brightness < 255) {
    analogWrite(status_blue, status_brightness);
    delay(10);
    status_brightness++;
  }
}

void loop() {
  analogWrite(status_blue, 255);
//  static float in = 4./712;
//  float out;/
  
  pan = analogRead(joyX);
  pan = map(pan, 0, 1023, 90, 400);
  smoothedPan = (pan * .02) + (panPrev * .98);
  panPrev = smoothedPan;
  HCPCA9685.Servo(2,smoothedPan);

  tilt = analogRead(joyY);
  tiltLeft = map(tilt, 0, 1023, 50, 350);
  smoothedTiltLeft = (tiltLeft * .02) + (tiltLeftPrev * .98);
  tiltLeftPrev = smoothedTiltLeft;
  tiltRight = map(tilt, 0, 1023, 350, 50);
  smoothedTiltRight = (tiltRight * .02) + (tiltRightPrev * .98);
  tiltRightPrev = smoothedTiltRight;
  HCPCA9685.Servo(0, smoothedTiltLeft);
  HCPCA9685.Servo(1, smoothedTiltRight);
  delay(5); // Learn how to remove this delay so LED can pulse

//  in = in + 0.0005;/
//  if (in > 10.995)/
//    in = 4.712;/
//  out = sin(in) * 127.5 + 127.5;/
//  analogWrite(status_blue, out);/
}
