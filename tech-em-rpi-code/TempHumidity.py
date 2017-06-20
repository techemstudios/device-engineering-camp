import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 4

def read_temp_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temp_f = temperature * 9.0 / 5.0 + 32.0
    return temperature, temp_f, humidity
