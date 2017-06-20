# Remember, everything after a # is a comment
# Comments are here for humans to explain code to
# other humans. Anything after a # is ignored by
# the computer

# Use the imports you have for the leds
# For example: from led import *\
from led import *
import time


def dash():
    red_led(1)
    print("-")
    time.sleep(.5)
    red_led(0)

def dot():
    red_led(1)
    print(".")
    time.sleep(.25)
    red_led(0)

def morse_a():
    dot()
    dash()

def morse_b():
    dash()
    dot()
    dot()
    dot()

def morse_c():
    dash()
    dot()
    dash()
    dot()

def morse_d():
    dash()
    dot()
    dot()

def morse_e():
    dot()

def morse_t():
    dash()

def morse(character):
    try:
        if character != " ":
            globals()["morse_"+character.lower()]()
    except KeyError:
        print(character + " not defined in morse yet."),


for i in range(10):
    print("Type in text to convert to morse code.")
    text = raw_input()
    for character in text:
        morse(character)
        print(" ")
