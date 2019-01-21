import RPi.GPIO as GPIO
from time import sleep


class OCPButtons(object):

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3, GPIO.HIGH)
        GPIO.setup(5, GPIO.HIGH)
        GPIO.setup(7, GPIO.HIGH)
        GPIO.setup(11, GPIO.HIGH)
        GPIO.setup(13, GPIO.HIGH)
        GPIO.setup(15, GPIO.HIGH)
        GPIO.setup(19, GPIO.HIGH)
        GPIO.setup(18, GPIO.HIGH)

    def RIGHTMAGAZINE(self, timePressed):
        GPIO.setup(3, GPIO.LOW)
        sleep(timePressed)
        GPIO.setup(3, GPIO.HIGH)

    def LEFTMAGAZINE(self, timePressed):
        GPIO.setup(5, GPIO.LOW)
        sleep(timePressed)
        GPIO.setup(5, GPIO.HIGH)

    def UP(self, timePressed):
        GPIO.setup(15, GPIO.LOW)
        sleep(timePressed)
        GPIO.setup(15, GPIO.HIGH)

    def RIGHT(self, timePressed):
        GPIO.setup(18, GPIO.LOW)
        sleep(timePressed)
        GPIO.setup(18, GPIO.HIGH)

    def ENTER(self, timePressed):
        GPIO.setup(11, GPIO.LOW)
        sleep(timePressed)
        GPIO.setup(11, GPIO.HIGH)

    def LEFT(self, timePressed):
        GPIO.setup(13, GPIO.LOW)
        sleep(timePressed)
        GPIO.setup(13, GPIO.HIGH)

    def DOWN(self, timePressed):
        GPIO.setup(19, GPIO.LOW)
        sleep(timePressed)
        GPIO.setup(19, GPIO.HIGH)

    def BACK(self, timePressed):
        GPIO.setup(7, GPIO.LOW)
        sleep(timePressed)
        GPIO.setup(7, GPIO.HIGH)

    def POWER(self, timePressed):
        pass
        #GPIO.setup(18, GPIO.LOW)
        #sleep(timePressed)
        #GPIO.setup(18, GPIO.HIGH)
