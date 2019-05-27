# Test script to generate output on serial port
# For use with FanController.ino
# Required: python >= 3.2, pySerial module
# Run: python3 FanControllerTest.py -p 'COM3' -b 9600

# Author: Pete Milne
# Date: 27-05-2019
# Version: 0.2

import serial, time, sys

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-p", "--port",
                    help="Serial comms port")
parser.add_argument("-b", "--baud",
                    help="Serial comms baud rate")

args = parser.parse_args()

# Open connection to device (port, baud rate, timeout)
device = serial.Serial(args.port, args.baud, timeout=.1)
#device = serial.Serial('COM3', 9600, timeout=.1)

time.sleep(2) # Allow connection to establish

# Set test values
test_speeds = [['   0kph', b'0\n'],
               ['   2kph', b'2\n'],
               [' 850kph', b'850\n'],
               ['1000kph', b'1000\n'],
               ['1200kph', b'1200\n'],
               ['3000kph', b'3000\n']]

# Run test
while True:
	for speed, kpm in test_speeds:
            device.write(kpm)
            print(speed, kpm)
            time.sleep(1)


