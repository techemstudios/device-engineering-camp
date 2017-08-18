# Remember, everything after a # is a comment
# Comments are here for humans to explain code to
# other humans. Anything after a # is ignored by
# the computer

# Use the imports you have for the leds
# For example: from led import *\
from led import *
import time

def dash():
    all_led(1)
    print("-")
    time.sleep(.5)
    all_led(0)

def dot():
    all_led(1)
    print(".")
    time.sleep(.25)
    all_led(0)

def morse_a():
    dot()
    dash()

def morse_l():
    dot()
    dash()
    dot()
    dot()

def morse_e():
    dot()

def morse_x():
    dash()
    dot()
    dot()
    dash()
def morse(character):
    try:
        if character != " ":
            globals()["morse_"+character.lower()]()
        except KeyError:
            print(character + " not defined in morse yet."),

for i in range(10):
    print("Type in text to convert ot morse code.")
    text = raw_input()
    for character in text:
        morse(character)
        print(" ")
