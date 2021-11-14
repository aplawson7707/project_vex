const int status_red = 2;
const int status_green = 3;
const int status_blue = 4;

void setup() {
  Serial.begin(9600);
  Serial.println("Initializing...");

  int status_brightness = 0;
  while (status_brightness < 255) {
    analogWrite(status_blue, status_brightness);
    delay(10);
    status_brightness++;
  }
  Serial.println("Status LED is online...");
}

void loop() {
  analogWrite(status_blue, 255);
//  Everything below this line is for making the status led pulse without delays.
//  static float in = 4.712;
//  float out;
//
//  //do input, etc. here - as long as you don't pause, led will pulse
//
//  in = in + 0.0005;
//  if (in > 10.995)
//    in =  4.712;
//  out = sin(in) * 127.5 + 127.5;
//  analogWrite(status_blue, out);
}
