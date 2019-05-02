#include <wiringPi.h>
#include <stdio.h>

#define LEDPIN 0

int main() {
  if (wiringPiSetup() == -1) {
    printf("Setup wiringPi Faild!");
    return -1;
  }

  pinMode(LEDPIN, OUTPUT);
  printf("\n");
  printf("\n");
  printf("****************************|\n");
  printf("|  LED Blink                |\n");
  printf("|  -----------------------  |\n");
  printf("|  LED connect to GPIO 0    |\n");
  printf("|  LED will blink at 500ms  |\n");
  printf("****************************|\n");

  while(1) {
    digitalWrite(LEDPIN, LOW);
    printf("...LED OFF\n");
    printf("\n");
    delay(500);
    digitalWrite(LEDPIN, HIGH);
    printf("LED ON...\n");
    printf("\n");
    delay(500);
  }
  return 0;
}
