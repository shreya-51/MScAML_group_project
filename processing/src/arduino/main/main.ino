#include "ArduinoBLE.h"
#include "SerialTransfer.h"
#include "pitches.h"

SerialTransfer myTransfer;

int Analog_Input_0 = A0; // Analog output of the sensor
int Analog_Input_1 = A1; // Analog output of the sensor
int Digital_Input = 3; // Digital output of the sensor
int microphone_output_0 = 0;
int microphone_output_1 = 0;


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
  pinMode(Digital_Input, INPUT);
       
  Serial.begin(9600);  //  Serial output with 9600 bps

   // iterate over the notes of the melody:

}
  
//  The program reads the current values of the input pins
// and outputs it on the serial output
void loop()
{
  //int Digital;
    for (int thisNote = 0; thisNote < 8; thisNote++) {

    // to calculate the note duration, take one second divided by the note type.

    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.

    int noteDuration = 1000 / noteDurations[thisNote];

    tone(2, melody[thisNote], noteDuration);

    // to distinguish the notes, set a minimum time between them.

    // the note's duration + 30% seems to work well:

    int pauseBetweenNotes = noteDuration * 1.30;

    delay(pauseBetweenNotes);

    // stop the tone playing:

    noTone(2);

  }
    
  //Current values are read out, converted to the voltage value...
  microphone_output_0 =  analogRead(Analog_Input_0);   //*  (5.0 / 1023.0);
  microphone_output_1 =  analogRead(Analog_Input_1);
  //Digital = digitalRead(Digital_Input) ;
  Serial.print(microphone_output_0);
  Serial.print(" ");
  Serial.println(microphone_output_1);
  
}
