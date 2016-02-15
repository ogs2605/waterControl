import RPi.GPIO as gpio
import time

outputPin = 21

gpio.setmode(gpio.BCM)
gpio.setup(outputPin, gpio.OUT)

print "Setting pin", outputPin, "to OFF"
gpio.output(outputPin, False)

gpio.cleanup()



