#!/usr/bin/python3

import serial
import time
import random

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 57600, timeout=1)
    ser.reset_input_buffer()

    while True:
        # if ser.in_waiting > 0:
        #     line = ser.readline().decode('utf-8').rstrip()
        #     print(line)
        number = random.randint(1, 5)
        ser.write(str(number).encode('utf-8'))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
