import RPi.GPIO as GPIO
import time

# set 8 pins for 8 leds
LedPins = [17, 18, 27, 22, 23, 24, 25, 4]

def print_message():
  print('')
  print('****************************|')
  print('|  Flow blink LEDs          |')
  print('|  -----------------------  |')
  print('|  LEDs will flow blinking  |');
  print('****************************|')
  print('Program is running...')
  print('Please press Ctrl+C to end the program...')


def setup():
  GPIO.setwarnings(False)

  # set the gpio modes to BCM numbering
  GPIO.setmode(GPIO.BCM)

  # set LED pins mode to output, and initial level LOW(0V)
  GPIO.setup(LedPins, GPIO.OUT, initial=GPIO.HIGH)

def main():
  # print info
  print_message()

  while True:
    for pin in LedPins:
      GPIO.output(pin, GPIO.LOW)
      time.sleep(0.2)
      GPIO.output(pin, GPIO.HIGH)
      pass

    for pin in reversed(LedPins):
      GPIO.output(pin, GPIO.LOW)
      time.sleep(0.2)
      GPIO.output(pin, GPIO.HIGH)

    pass
  pass

def destroy():
  # turn off LED
  GPIO.output(LedPins, GPIO.LOW)

  # release resource
  GPIO.cleanup()

if __name__ == '__main__':
  setup()
  try:
    main()
  except KeyboardInterrupt:
    destroy()

