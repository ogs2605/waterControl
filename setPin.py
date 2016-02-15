import RPi.GPIO as gpio
import time

def setPin21On():
    print "setGpioOutPinState: setPin21On"
    setGpioOutPinState(21, True)
    
    
def setGpioOutPinState(pin, isOn):
    gpio.setmode(gpio.BCM)
    gpio.setup(pin, gpio.OUT)

    if isOn == True:
        print "setGpioOutPinState: Setting pin", pin, "to ON"
    else:
        print "setGpioOutPinState: Setting pin", pin, "to OFF"
    
    gpio.output(pin, isOn)

    gpio.cleanup()

