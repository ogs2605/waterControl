import RPi.GPIO as gpio
import time

def setPin():
    outputPin = 21

    gpio.setmode(gpio.BCM)
    gpio.setup(outputPin, gpio.OUT)

    print "Setting pin", outputPin, "to ON"
    gpio.output(outputPin, True)

    gpio.cleanup()
