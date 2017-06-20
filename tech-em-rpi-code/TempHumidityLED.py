from TempHumidity import *
from led import *
while(1):
    read_temp_humidity()
    if temp_f >= 70:
        green_led(1)
    else:
        green_led(0)
    if humidity >= 70:
        red_led(1)
    else:red_led(0)
