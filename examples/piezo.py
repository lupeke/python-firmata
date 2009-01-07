#! /usr/bin/env python
"""
Piezo example
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

from firmata import * 

a = Arduino('/dev/tty.usbserial-A1001NQe') # Put your serial port here
a.pin_mode(2, OUTPUT)

while True:
    a.parse()
    print a.analog_read(2) # Reading from analog pin #2