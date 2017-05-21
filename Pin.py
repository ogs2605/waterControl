'''
Created on 21 May 2017

@author: James
'''
import setPin as setPin

class Pin(object):
    
    def __init__(self, pinNumber):
        self.pinNumber = pinNumber
        
    def on(self):
        setPin.setGpioOutPinState(self.pinNumber,True)
        print ("Pin: pin " + self.pinNumber + " on received....")
        
    def off(self):
        setPin.setGpioOutPinState(self.pinNumber,False)
        print ("Pin: pin " + self.pinNumber + " off received....")
