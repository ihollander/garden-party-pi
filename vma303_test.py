import RPi.GPIO as GPIO
import time
import datetime

# initialize GPIO
GPIO.setwarnings(false)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:
  print("Water sensor: ", GPIO.input(17))

  time.sleep(1)
