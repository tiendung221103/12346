import RPi.GPIO as GPIO # type: ignore
import time

class Device:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

    def setLock(self, state: bool):
        GPIO.setup(11, GPIO.OUT)
        if state:
            GPIO.output(11, GPIO.HIGH)
            time.sleep(4)
            GPIO.output(11, GPIO.LOW)
