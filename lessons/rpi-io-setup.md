Title: Notes on setting up pis for I/O lessons
Date: 2015-08-21
Category: Notes
Tags: raspberry pi, adafruit, python
Author: Wray Mills
Summary: Some notes and code

Just dropping in some code for instructors, students, and everyone
[updated August 2015].

### Initial Config
For classes and camps, we always start with an SD card that has
raspian (the Operating System) pre-installed. Of course, for the last
camp, we started with blank SD cards! So, on that first day, we were
actually loading the OS on your cards.

After logging in, we then ran
```bash
sudo raspi-config
```

in order to extend the filesystem, set the correct time, and set the
correct keyboard.

We also configured your wi-fi adapter by running the gui

```bash
startx
```

and using the wifi settings to scan for networks, choose the network,
type in the password, and connect. Remember, you'll have to do this
for your home wireless netework. Try to run startx without sudo. If
the GUI doesn't come up, you may have to use sudo. When you are using
the LEDS or the temp sensor, you will have to run python as sudo.

### Config for LEDs, Minecraft and Temp sensor
In lieu of burning a pre-configured SD, we can run this script on a
raspbian pi (model 2 with pre-loaded raspian from Adafruit) in order to get python development tools, the
RPi GPIO library and the DHT library from Adafruit. Note, that this setup
assumes your pi has network (Internet) connectivity. You can type in
these commands separately, starting with the first line not containing
a #.

```python
#!/bin/sh
# Run this command using sudo

# Beforehand, you should expand filesystem, turn on ssh
# and of course configure network.

sudo apt-get update
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo easy_install -U distribute
sudo pip install --upgrade RPi.GPIO
sudo apt-get install build-essential
git clone git://github.com/adafruit/Adafruit_Python_DHT
cd Adafruit_Python_DHT
sudo python setup.py install
cd ..
```

### LEDs
So, for the Output portion of the I/O lesson (easier than input so you
may as well start here), assume a green LED is wired to #20 and a red
LED is wired to #21.

```python
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

```

So, a simple session to use these methods would look like this:

```python
sudo python
>>>from led import *
>>>green_led(1)
>>>red_led(1)
>>>green_led(0)
>>>red_led(0)
>>>quit()
```

### Extend the LED Morse Code output
We started a program that reads input from a user and converts that
input into LED morse code. Start with this snippet and see if you can
finish it -- let us know how you do!!

```python
# Remember, everything after a # is a comment
# Comments are here for humans to explain code to
# other humans. Anything after a # is ignored by
# the computer

# Use the imports you have for the leds
# For example: from led import *


def dash():
    #whatever code you already have here
    print("-"),

def dot():
    # whatever code you already have here
    print("."),

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


```

If you save this file as "morse_output.py" for example, you may run it
with:

```python
sudo python morse_output.py
```

### Input Sensor (Temp/Humidity Sensor including in your Tech Em kit)
For the Input part of the lesson, here is some code that provides a single simple method to
return temperature and humidity (from a DHT-22 temperature/humidity
sensor [wired to pin #4](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/wiring)).

```python
#
# Template code for temperature and humidity from an Adafruit DHT22
# sensor. Don't forget to update this file if you connect the DHT22 
# to another data pin,
# want to change the delay, or logic for mailing. 
# For example, you may only want to
# send notifications when certain thresholds are exceeded.
# 
# Code provided for Tech Em students and open under Gnu GPL
#
# Wray Mills
# 20141115
#

import os
import time
import Adafruit_DHT
# Tech Em mail utility
# from mailit import *

sensor = Adafruit_DHT.DHT22
pin = 4 

def read_temp_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temp_f = temperature * 9.0 / 5.0 + 32.0
    return temperature, temp_f, humidity

```

Launch python with sudo, import this file and call the method to get
the tuple of celsius temperature, fahrenheit temperature, and relative humidity.

![Rpi prototype board with DHT22 on one side and two LEDs on the other]({filename}/images/rpi-io.jpg)
