Title: Some Code for RPi temp sensing
Date: 2015-05-13
Category: Notes
Tags: raspberry pi, adafruit, python
Author: Wray Mills
Summary: Some notes and code

Just dropping in some code for students to use.

After wiring your DS18B20, you need to prep your pi for using
it. After logging in, do this:

```
sudo nano /boot/config.txt
```

And add this line to it:

```
dtoverlay=w1-gpio
```

Now, reboot your pi:

```
sudo reboot
```

Now, let's test the temp sensor with these commands:

```
sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices
ls
cd 28<tab>
cat w1_slave
```

You should see two lines with a "YES" at the end of the first line and
the temp reading at the end of the second. Once you've done this, go
ahead and

```
cd ~
sudo startx
```

and launch python2, create a new file and put the code below in
it. Save it as temp.py.



Here is the associated code that reads from the DS18B20 temp sensor.
~~~~~~
import os
import glob
import time
#from mailit import *
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
	
while True:
    print('The current temp is: %dC, %dF' % (read_temp()))
	#deliver('The current temp is: %dC, %dF' % (read_temp()))
	time.sleep(1500)

~~~~~~

This is a very simple/generic mailing routine. Uncomment the "from
mailit import *" and the function call to "deliver" in the above
routine to have your temp reading sent via email. You should save this
code in a file called mailit.py.

~~~~~~
# Simple smtp mail utility to be used by Tech Em students.
# This will run on the RPi with the Occidentalis install.
# Thus, it is a handy utility to use along with adafruit sensors
#
# 201406 Wray Mills
#

import subprocess
import smtplib
import socket

from email.mime.text import MIMEText
import datetime

### 
# Change to your settings
###
pi_name = 'wray-pi'
to = 'somebody@somewhere.com'

## Feel free to reuse the techem student relay
mail_user = 'student@techemstudios.com'
mail_password = 'pword-on-whiteboard'

def deliver ( message, subject = 'RPi output' ):
    smtpserver = smtplib.SMTP('smtpout.secureserver.net', 3535) # Use 587 for gmail
    smtpserver.ehlo()
    #smtpserver.starttls() # Uncomment this line for gmail
    smtpserver.login(mail_user, mail_password)
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = '(%s)%s' % (pi_name,mail_user)
    msg['To'] = to
    smtpserver.sendmail(mail_user, [to], msg.as_string())
    smtpserver.quit()
~~~~~~

