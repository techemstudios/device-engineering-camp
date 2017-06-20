import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

mc.postToChat("Hello Minecraft World")

import time

while(1):
    pos = mc.player.getTilePos()

    print(pos.x)
    print(pos.y)
    print(pos.z)

    from led import *

    if pos.y > 5:
        green_led(1)
    else:
        green_led(0)

    time.sleep(5)
