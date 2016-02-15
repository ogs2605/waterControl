import RPi.GPIO as gpio
import time

def setPin21On():
    print "setGpioOutPinState: setPin21On"
    setGpioOutPinState(21, True)
    
    
def setGpioOutPinState(pin, isOn):
    gpio.setmode(gpio.BCM)
    gpio.setup(pin, gpio.OUT)

    print "setGpioOutPinState: Setting pin", pin, "to ON"
    gpio.output(pin, isOn)

    gpio.cleanup()

