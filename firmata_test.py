# from pyfirmata import ArduinoMega
import pyfirmata
import time
import requests

board = pyfirmata.ArduinoMega("/dev/ttyACM0")
url = 'http://localhost:12101/api/text-to-speech?play=true'
headers = {
	'accept': 'audio/wav',
	'Content-Type': 'text/plain'
}
message = "Connection to motor cortex established. Articulation capabilities are online."

announce = requests.post(url, headers=headers, data=message)
# print(announce.status_code)

# board.digital[2].write(0)
LED = board.digital[2]
LED.mode = pyfirmata.PWM

pwm_counter = 0.01
increase_pwm = True

while True:
        if increase_pwm:
            pwm_counter += 0.01
            if pwm_counter >= 1:
                increase_pwm = False
        else:
            pwm_counter -= 0.01
            if pwm_counter <= 0:
                increase_pwm = True
        LED.write(pwm_counter)
        time.sleep(0.01)