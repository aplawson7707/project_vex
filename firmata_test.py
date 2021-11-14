from pyfirmata import ArduinoMega
import time

board = ArduinoMega("/dev/ttyACM0")

# loopTimes = input("How many times would you like the LED to blink?: ")
# print("Blinking " + loopTimes + "times.")

board.digital[2].write(1)
time.sleep(5)
board.digital[2].write(0)

# for x in range(int(loopTimes)):
# 	board.digital[4].write(1)
# 	time.sleep(1)
# 	board.digital[4].write(0)
# 	time.sleep(1)
