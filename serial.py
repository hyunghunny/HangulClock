# coding=UTF-8

# @brief {brief description]
#
# @author webofthink@snu.ac.kr
#
# code snippet from http://pyserial.sourceforge.net/shortintro.html
import serial
import io
ser = serial.serial_for_url('loop://', timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

sio.write(unicode("hello\n"))
sio.flush() # it is buffering. required to get the data out *now*
hello = sio.readline()
print hello == unicode("hello\n")