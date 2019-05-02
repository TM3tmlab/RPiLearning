import RPi.GPIO as GPIO
import time

# set GPIO 0 as LED pin
LEDPIN = 17

def print_message():
  print('')
  print('****************************|')
  print('|  LED Blink                |')
  print('|  -----------------------  |')
  print('|  LED connect to GPIO 0    |')
  print('|  LED will blink at 500ms  |')
  print('****************************|')
  print('Program is running...')
  print('Please press Ctrl+C to end the program...')


def setup():
  GPIO.setwarnings(False)

  # set the gpio modes to BCM numbering
  GPIO.setmode(GPIO.BCM)

  # set LED pins mode to output, and initial level LOW(0V)
  GPIO.setup(LEDPIN, GPIO.OUT, initial=GPIO.LOW)

def main():
  # print info
  print_message()

  while True:
    GPIO.output(LEDPIN, GPIO.HIGH)
    print('...LED ON\n')
    time.sleep(0.5)

    GPIO.output(LEDPIN, GPIO.LOW)
    print('...LED OFF\n')
    time.sleep(0.5)

    pass
  pass

def destroy():
  # turn off LED
  GPIO.output(LEDPIN, GPIO.LOW)

  # release resource
  GPIO.cleanup()

if __name__ == '__main__':
  setup()
  try:
    main()
  except KeyboardInterrupt:
    destroy()

