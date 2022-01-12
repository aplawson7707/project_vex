#!/usr/bin/python3

# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name

import serial,time
from speak import speak

if __name__ == '__main__':

    speak("Establishing link with motor cortex.")
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
        time.sleep(0.1) #wait for serial to open
        if arduino.isOpen():
            speak("Cortex link established.")
            print("{} connected!".format(arduino.port))
            try:
                while True:
                    cmd=input("Enter command : ")
                    arduino.write(cmd.encode())
                    #time.sleep(0.1) #wait for arduino to answer
                    while arduino.inWaiting()==0: pass
                    if  arduino.inWaiting()>0: 
                        answer=arduino.readline()
                        speak(answer)
                        print(answer)
                        arduino.flushInput() #remove data after reading
            except KeyboardInterrupt:
                speak("Disconnecting from motor cortex.")
                print("KeyboardInterrupt has been caught.")
