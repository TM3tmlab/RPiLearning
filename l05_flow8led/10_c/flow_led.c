#include <wiringPi.h>
#include <stdio.h>

// for flow delay time(msec)
#define DELAY_TIME 66

void setUp(void) {
  for (int i = 0; i < 8; i += 1) {
    pinMode(i, OUTPUT);
    digitalWrite(i, HIGH);
  }
  return;
}

void turnOn(int channel) {
  digitalWrite(channel, LOW);
  return;
}

void turnOff(int channel) {
  digitalWrite(channel, HIGH);
  return;
}

int main(void) {
  if (wiringPiSetup() == -1) {
    printf("Setup wiringPi Faild!");
    return -1;
  }

  setUp();

  printf("|***************************|\n");
  printf("|  Flow Blink LEDs          |\n");
  printf("|  -----------------------  |\n");
  printf("|  LEDs will flow blinking  |\n");
  printf("|***************************|\n");

  while(1) {
    for (int i = 0; i < 8; i+= 1) {
      turnOn(i);
      delay(DELAY_TIME);
      turnOff(i);
    }
    for (int i = 7; i >= 0; i-= 1) {
      turnOn(i);
      delay(DELAY_TIME);
      turnOff(i);
    }
  }
  return 0;
}

