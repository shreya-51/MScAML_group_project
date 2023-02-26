#include "ArduinoBLE.h"
#include "SerialTransfer.h"


SerialTransfer myTransfer;

int micro_0 = A0; // Analog output of the sensor
int micro_1 = A1;
int Digital_Input = 3; // Digital output of the sensor
int microphone0_out = 0;
int microphone1_out = 0;


void setup() {
  pinMode(micro_0, INPUT);
  pinMode(micro_1, INPUT);
  pinMode(Digital_Input, INPUT);
       
  Serial.begin(9600);  //  Serial output with 9600 bps
}
  
//  The program reads the current values of the input pins
// and outputs it on the serial output
void loop()
{
  //int Digital;
    
  //Current values are read out, converted to the voltage value...
  microphone0_out =  analogRead(micro_0); 
  microphone1_out =  analogRead(micro_1); 
  //Digital = digitalRead(Digital_Input);
  Serial.print(microphone0_out);
  Serial.print(" ");
  Serial.print(microphone1_out);
  Serial.println(" ");
  delay(10);
}
