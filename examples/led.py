"""LED example"""

from firmata import *

a = Arduino('/dev/tty.usbserial-A1001NQe')
a.pin_mode(13, OUTPUT)
a.delay(2)

while True:
    a.digital_write(13, HIGH)
    a.delay(2)
    a.digital_write(13, LOW)
    a.delay()