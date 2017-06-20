Title: Notes on setting up pis to use Minecraft API
Date: 2015-05-20
Category: Notes
Tags: raspberry pi, python, Minecraft
Author: Wray Mills
Summary: Some notes and code

Just dropping in some code for instructors, students, and everyone
[for Raspberry Pi 2].

Let's grab some Python libraries that can connect to your Minecraft World.
Login to your pi and launch the GUI:

```
startx
```

Open up a browser and go to:

```
www.wiley.com/go/adventuresinminecraft
```
and download the starter kit. Choose "open" and open the program
called Xarchiver. Click Action -> Extract on the Xarchiver menu. Type
/home/pi in the Extract to: text box.

Now, open up IDLE (Python) and create a new program file. You'll want
to save this file in the "My Adventures" folder you just created. You
can name this first file "hello_minecraft.py". This actually assumes
you have already done the LED input lesson and have a file led.py that
you have copied into your "My Adventures" folder. Finally, since this
code uses the raspberry pi I/O, you'll need to open up a new terminal
window (LX Terminal), change directory (using "cd") to "My Adventures"
and run the file with sudo.

```python

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

```

So, running this would go something like this:

```bash
cd "My Adventures"
sudo python hello_minecraft.py
```

Want to build something?

```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

import mcpi.block as block

pos = mc.player.getTilePos()

for y in range(150):
    mc.setBlock(pos.x+2,pos.y+y,pos.z,block.TNT.id)
```

Here is another cool program to try.

```python
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

bridge = []

def buildBridge():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x,pos.y-1,pos.z)
    if b == block.AIR.id or b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id:
        mc.setBlock(pos.x,pos.y-1,pos.z,block.GLASS.id)
        coordinate = [pos.x,pos.y-1,pos.z]
        bridge.append(coordinate)

    elif b != block.GLASS.id:
        if len(bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate[0],coordinate[1],coordinate[2],block.AIR.id)
            time.sleep(0.25)

while True:
    time.sleep(0.25)
    buildBridge()

```

And while you are at it, can you post the current temp to the chat??
The hint here is that you should copy your temp.py file into your
"MyAdventures" sub-directory, comment-out the deliver method and
update the print method (at the end of the file) to postToChat. And,
don't forget to do the minecraft setup (imports and creation) in order
to postToChat.

What else can you do? Do you want to do? You all now have temp input,
led output, minecraft control, and outbound email capabilities!!

