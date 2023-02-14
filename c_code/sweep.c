#include <Arduino.h>

int speakerPin = 9;
int frequency = 20;
int sweepDuration = 5000; // 5 seconds
int increment = 5;

void setup() {
  pinMode(speakerPin, OUTPUT);
}

void loop() {
  for (frequency = 20; frequency <= 20000; frequency += increment) {
    tone(speakerPin, frequency, sweepDuration/increment);
    delay(sweepDuration/increment);
  }
}
