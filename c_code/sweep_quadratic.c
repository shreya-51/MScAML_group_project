#include <Arduino.h>

int speakerPin = 9;
int min_freq = 20;
int max_freq = 20000;
int sweepDuration = 5000; // 5 seconds
int increment = 1;

int num_freq = (max_freq - min_freq) / 5;

void setup() {
  pinMode(speakerPin, OUTPUT);
}

void loop() {
  while(frequency < max_freq){
    frequency = min_freq + pow(increment, 2);
    tone(speakerPin, frequency, sweepDuration/num_freq);
    delay(sweepDuration/num_freq);
    increment++;
  }
}