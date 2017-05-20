import RPi.GPIO as gpio
import time

def setGpioOutPinState(pin, isOn):
    gpio.setmode(gpio.BCM)
    gpio.setup(pin, gpio.OUT)
    
    if isOn == True:
        print (time.localtime(), ": setGpioOutPinState: Setting pin", pin, "to ON")
    else:
        print ("setGpioOutPinState: Setting pin", pin, "to OFF")
    
    gpio.output(pin, isOn)

    
