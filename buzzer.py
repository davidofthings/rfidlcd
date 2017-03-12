import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)

loop_count = 0

def buzz():
	GPIO.output(23,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(23,GPIO.LOW)
	time.sleep(1)
