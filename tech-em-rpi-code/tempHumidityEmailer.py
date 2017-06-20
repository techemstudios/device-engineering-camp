import smtplib
from tempHumidity import *


server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

username = #enter email address here
password = #enter password here
msg = read_temp_humidity()
recipient = #enter recipient here

server.login(username, password)
server.sendmail(username, recipient, msg)
