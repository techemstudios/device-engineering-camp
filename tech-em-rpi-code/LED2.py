import RPi.GPIO as GPIO

DEBUG = 1

GPIO.setmode(GPIO.BCM)

GREEN_LED = 4
RED_LED = 5
BLUE_LED = 26
ALL_LED = [4, 5, 26]

GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.setup(ALL_LED, GPIO.OUT)

def green_led(state):
    GPIO.output(GREEN_LED,state)

def red_led(state):
    GPIO.output(RED_LED,state)
    
def blue_led(state):
    GPIO.output(BLUE_LED,state)
    
def all_led(state):
  GPIO.output(ALL_LED,state)
