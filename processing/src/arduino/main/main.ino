#include "ArduinoBLE.h"
#include "SerialTransfer.h"
#include "pitches.h"

SerialTransfer myTransfer;

int Analog_Input_0 = A0; // Analog output of the sensor
int Analog_Input_1 = A1; // Analog output of the sensor
int Analog_Input_2 = A2; // Analog output of the sensor
int Analog_Input_3 = A3; // Analog output of the sensor
int Digital_Input = 2; // Digital output of the sensor
int microphone_output_0 = 0;
int microphone_output_1 = 0;
int microphone_output_2 = 0;
int microphone_output_3 = 0;
int analog_test = A7;
float start;

int min_frequency = 20;
int max_frequency = 5000;
int increment = 10;

int num_freq = (max_frequency - min_frequency) / increment;

int sweepDuration = 5000; // 5 seconds
int count = 0;

unsigned long myTime1;
unsigned long myTime2;
unsigned long myTime3 = 0;

unsigned long temp1;
unsigned long temp2;

unsigned long myTime4;
unsigned long myTime5;
unsigned long threshold = 100;


void setup() {
  pinMode(Analog_Input_0, INPUT);
  pinMode(Analog_Input_1, INPUT);
  pinMode(Analog_Input_2, INPUT);
  pinMode(Analog_Input_3, INPUT);
  pinMode(Digital_Input, OUTPUT);
       
  Serial.begin(57600);  //  Serial output with 9600 bps

  //myTime1 = millis();
  //sweep();  //send the sweep, should take 3ms
  //myTime2 = millis();
  //Serial.println(myTime2 - myTime1);

//  myTime4 = millis();
//  while (myTime3 < threshold)
//  {
//    temp1 = millis();
//    listen(); // listen to the echos, should take 100ms
//    temp2 = millis();
//    myTime3 += temp2 - temp1;
//  }
//  myTime5 = millis();
//  Serial.println(myTime5 - myTime4);

}
  
//  The program reads the current values of the input pins
// and outputs it on the serial output
void loop()
{
  while (count < 1) {
    echo_signal();
    count += 1;
  }
  listen();
}

void sweep()
{
    for (int frequency = 20; frequency <= 5000; frequency += increment) 
    {
      tone(Digital_Input, frequency, sweepDuration/num_freq);
      delay(2);
      listen();
    }
}


void echo_signal() {
  
  tone(Digital_Input, 1000, 1500);
  //listen();
}


void listen()
{
    // Current values are read out, converted to the voltage value...
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

}
