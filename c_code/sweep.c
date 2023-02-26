#include <Arduino.h>

int speakerPin = 9;
int min_freq = 20;
int max_freq = 20000;
int sweepDuration = 5000; // 5 seconds
int increment = 5;

int num_freq = (max_freq - min_freq) / increment;

void setup() {
  pinMode(speakerPin, OUTPUT);
}

void loop() {
  for (frequency = min_freq; frequency <= max_freq; frequency += increment) {
    tone(speakerPin, frequency, sweepDuration/num_freq);
    delay(sweepDuration/num_freq);
  }
}