import RPi.GPIO as GPIO

DEBUG = 1

GPIO.setmode(GPIO.BCM)
GREEN_LED = 20
RED_LED = 21
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)


def green_led(state):
    GPIO.output(GREEN_LED,state)

def red_led(state):
    GPIO.output(RED_LED,state)
