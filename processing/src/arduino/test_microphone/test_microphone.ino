#include "ArduinoBLE.h"
#include "SerialTransfer.h"


SerialTransfer myTransfer;

int Analog_Input = A0; // Analog output of the sensor
int Digital_Input = 3; // Digital output of the sensor
int microphone_output = 0;


void setup() {
  pinMode(Analog_Input, INPUT);
  pinMode(Digital_Input, INPUT);
       
  Serial.begin(9600);  //  Serial output with 9600 bps
}
  
//  The program reads the current values of the input pins
// and outputs it on the serial output
void loop()
{
  int Analog;
  //int Digital;
    
  //Current values are read out, converted to the voltage value...
  Analog =  analogRead(Analog_Input);   //*  (5.0 / 1023.0); 
  //Digital = digitalRead(Digital_Input) ;
  microphone_output = Analog;
  Serial.println(microphone_output);
  
  delay(10) ;
}
