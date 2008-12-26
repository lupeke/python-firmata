import firmata

conn = firmata.Arduino('/dev/tty.usbserial-A4001JwZ')

conn.pin_mode(11, firmata.OUTPUT)

while 1:
    conn.iterate()
    print conn.analog_read(1)
    conn.digital_write(11, firmata.HIGH)