const int sampleWindow = 50; // Sample window width in mS (50 mS = 20Hz)
const int LEDsampleWindow = 100;
const int leftLED = 7;
const int rightLED = 8;
unsigned int leftSample;
unsigned int rightSample;
String direction;

void setup() 
{
   Serial.begin(115200);
}


void loop() 
{
   unsigned long startMillis= millis();  // Start of sample window
   unsigned int leftPeakToPeak = 0;   // peak-to-peak level
   unsigned int rightPeakToPeak = 0;

   unsigned int leftSignalMax = 0;
   unsigned int leftSignalMin = 1024;
   unsigned int rightSignalMax = 0;
   unsigned int rightSignalMin = 1024;

   // collect data for 50 mS
   while (millis() - startMillis < sampleWindow)
   {
      leftSample = analogRead(0);
      if (leftSample < 1024)  // toss out spurious readings
      {
         if (leftSample > leftSignalMax)
         {
            leftSignalMax = leftSample;  // save just the max levels
         }
         else if (leftSample < leftSignalMin)
         {
            leftSignalMin = leftSample;  // save just the min levels
         }
      }
      rightSample = analogRead(1);
      if (rightSample < 1024)  // toss out spurious readings
      {
         if (rightSample > rightSignalMax)
         {
            rightSignalMax = rightSample;  // save just the max levels
         }
         else if (rightSample < rightSignalMin)
         {
            rightSignalMin = rightSample;  // save just the min levels
         }
      }
   }
   leftPeakToPeak = leftSignalMax - leftSignalMin;  // max - min = peak-peak amplitude
   double leftVolts = (leftPeakToPeak * 5.0) / 1024;  // convert to volts
   rightPeakToPeak = rightSignalMax - rightSignalMin;
   double rightVolts = (rightPeakToPeak * 5.0) / 1024;
   double delta = (leftVolts - rightVolts) * 50;

   Serial.print(String("Left: ") + leftVolts);
   Serial.print(",");
   Serial.print(String("Right: ") + rightVolts);
   Serial.print(",");
   while (millis() - startMillis < LEDsampleWindow)
   {
    if (delta > 5)
    {
      direction = "Left";
      analogWrite(leftLED, 255);
    }
    else if (delta < -5)
    {
      direction = "Right";
      analogWrite(rightLED, 255);
    }
    else {
      direction = "Center";
      analogWrite(leftLED, 0);
      analogWrite(rightLED, 0);
    }
   }
   Serial.println(direction);
}
