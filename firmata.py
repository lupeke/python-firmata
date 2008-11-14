#! /usr/bin/env python

"""
python-firmata is a python interface for the Arduino's firmata protocol
Copyright (C) 2008  laboratorio (info@laboratorio.us)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__version__ = "0.1"

import serial

DIGITAL_MESSAGE = 0x90 # send data for a digital port
ANALOG_MESSAGE = 0xE0 # send data for an analog pin (or PWM)
REPORT_ANALOG = 0xC0 # enable analog input by pin #
REPORT_DIGITAL = 0xD0 # enable digital input by port
SET_PIN_MODE = 0xF4 # set a pin to INPUT/OUTPUT/PWM/etc
REPORT_VERSION = 0xF9 # report firmware version
SYSTEM_RESET = 0xFF # reset from MIDI
START_SYSEX = 0xF0 # start a MIDI SysEx message
END_SYSEX = 0xF7 # end a MIDI SysEx message

# pin modes
INPUT = 0
OUTPUT = 1
PWM = 2
SERVO = 3

LOW = 0
HIGH = 1
MAX_DATA_BYTES = 32

class Arduino:
    
    def __init__(self, port, baudrate=57600):
        """"""
        self.serial = serial.Serial(port, baudrate, timeout=0.02)
        self.wait_for_data = 0
        self.exec_multibyte_cmd = 0
        self.multibyte_channel = 0
        self.stored_input_data = []
        self.digital_output_data =  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
        self.digital_input_data  = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
        self.analog_input_data = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
        self.major = 0
        self.minor = 0
        self.__report()
        
    def __str__(self):
        return "Arduino: %s" % self.serial.port

    def pin_mode(self, pin, mode):
        """
        """
        self.serial.write(chr(SET_PIN_MODE))
        self.serial.write(chr(pin))
        self.serial.write(chr(mode))

    def digital_read(self, port):
        """
        Reading from digital port 
        """
        pass

    def digital_write(self, port, value):
        """
        Writing to a digital port
        """
        pass

    def analog_read(self, pin):
        """
        Reading from analog pin
        """
        pass

    def analog_write(self, pin, value):
        """
        Writing to a analog pin
        """
        pass

    def loop(self):
        """
        """
        pass
        
    def __process(self, data):
        """
        Processing input data
        """
        pass

    def available(self):
        """"""
        return self.serial.isOpen()

    def __report(self):
        """
        Reporting analog and digital pins
        """
        enable = 1
        for port in range(14):
            self.serial.write(chr(REPORT_DIGITAL + port))
            self.serial.write(chr(enable))
            
        for pin in range(6):
            self.serial.write(chr(REPORT_ANALOG + pin))
            self.serial.write(chr(enable))