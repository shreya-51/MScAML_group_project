#include "ArduinoBLE.h"
#include "SerialTransfer.h"
#include "pitches.h"

SerialTransfer myTransfer;

int Analog_Input_0 = A0; // Analog output of the sensor
int Analog_Input_1 = A1; // Analog output of the sensor
int Analog_Input_2 = A2; // Analog output of the sensor
int Analog_Input_3 = A3; // Analog output of the sensor
int Digital_Input = 3; // Digital output of the sensor
int microphone_output_0 = 0;
int microphone_output_1 = 0;
int microphone_output_2 = 0;
int microphone_output_3 = 0;

int frequency = 20;
int sweepDuration = 3; // 5 seconds
int increment = 5;


int melody[] = {

  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int noteDurations[] = {

  4, 8, 8, 4, 4, 4, 4, 4
};

void setup() {
  pinMode(Analog_Input_0, INPUT);
  pinMode(Analog_Input_1, INPUT);
  pinMode(Analog_Input_2, INPUT);
  pinMode(Analog_Input_3, INPUT);
  pinMode(Digital_Input, INPUT);
       
  Serial.begin(9600);  //  Serial output with 9600 bps

   // iterate over the notes of the melody:

}
  
//  The program reads the current values of the input pins
// and outputs it on the serial output
void loop()
{

  for (frequency = 20; frequency <= 20000; frequency += increment) {
    tone(Digital_Input, frequency, sweepDuration/increment);
    //Current values are read out, converted to the voltage value...
    microphone_output_0 =  analogRead(Analog_Input_0);   //*  (5.0 / 1023.0);
    microphone_output_1 =  analogRead(Analog_Input_1);
    microphone_output_2 =  analogRead(Analog_Input_2);   //*  (5.0 / 1023.0);
    microphone_output_3 =  analogRead(Analog_Input_3);
    Serial.print(microphone_output_0);
    Serial.print(" ");
    Serial.print(microphone_output_1);
    Serial.print(" ");
    Serial.print(microphone_output_2);
    Serial.print(" ");
    Serial.print(microphone_output_3);
    Serial.println(" ");
    delay(sweepDuration/increment);
  }
  
}
