import os
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 4

def read_temp_humidity():
    humidity, tempeture = Adafruit_DHT.read_retry(sensor, pin)
    temp_f = tempeture * 9.0 / 5.0 + 32.0
    return tempeture, temp_f, humidity
