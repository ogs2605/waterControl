'''
Created off 21 May 2017

@author: James
'''
import setPin as setPin
import logging

class Pin(object):
    '''
    Concept of a GPIO pin with a state
    '''

    def __init__(self, pinNumber):
        self.__pinNumber = pinNumber
        self.__="UNKNOWN!"
        self.__isOn = None
        self.off()
        logging.info("Pin() " + str(self.__pinNumber) + " created")
        
    def on(self):
        self.__isOn = True
        self.__currentState = "ON"
        setPin.setGpioOutPinState(self.__pinNumber, True)
        print ("Pin.on(): pin ", self.__pinNumber)
        logging.info('Doing something')

    def off(self):
        self.__isOn=False
        self.__currentStateStr = "OFF"
        setPin.setGpioOutPinState(self.__pinNumber, False)
        print ("Pin.off(): pin ", self.__pinNumber)
    
    def getIsOn(self):
        return self.__isOn
    
    def getStateStr(self):
        return self.__currentStateStr