import pyfirmata
import time

if __name__ == '__main__':
	board = pyfirmata.Arduino('/dev/ttyACM0')
	print("Communication Successful")

	while True:
		board.digital[13].write(1)
		time.sleep(1)
		board.digital[13].write(0)
		time.sleep(1)
