import RPi.GPIO as GPIO
import time
 
DEBUG = 1
 
GPIO.setmode(GPIO.BCM)
GREEN_LED = 23
RED_LED = 12
BLUE_LED = 21
RED2_LED = 18
BLUE2_LED = 25
RED3_LED = 18
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.setup(RED2_LED, GPIO.OUT)
GPIO.setup(BLUE2_LED, GPIO.OUT)
GPIO.setup(RED3_LED, GPIO.OUT)


def green_led(state):
    GPIO.output(GREEN_LED,state)

def red_led(state):
    GPIO.output(RED_LED,state)

def blue_led(state):
    GPIO.output(BLUE_LED,state)

def red2_led(state):
    GPIO.output(RED2_LED,state)

def blue2_led(state):
    GPIO.output(BLUE2_LED,state)
    
def red3_led(state):
    GPIO.output(RED3_LED,state)


def all_led(state):
    GPIO.output(BLUE_LED,state)
    GPIO.output(GREEN_LED,state)
    GPIO.output(RED_LED,state)
    GPIO.output(RED2_LED,state)
    GPIO.output(BLUE2_LED,state)
    GPIO.output(RED3_LED,state)

def flash():
    for i in range(150):
        all_led(0)
        time.sleep(0.2)
        all_led(1)
        time.sleep(0.2)
