'''
Created off 26 May 2017

@author: James
'''
from Pin import Pin
import datetime
import sched
import time
import threading

class TimedPin(object):
    '''
    Concept of a __pin that remains off for a certain amount of time then turns off...
    '''      
    def __init__(self, pinNumber):
        self.__pin  = Pin(pinNumber)
        self.__turnOffTime = datetime.datetime.utcnow()
        self.__pinOffEventId = 0
        self.__scheduler = sched.scheduler(time.time, time.sleep)
        self.__threadObj = None
        
    def increaseTimeOn(self):
                
        if self.__pin.getIsOn() == False:
            # __pin was off... 
            self.startSchedulerThread()
            now = datetime.datetime.utcnow()
            self.__turnOffTime = now + datetime.timedelta(0, 10)
            self.__pinOffEventId = self.__scheduler.enter(10, 1, self.turnOff, ())
            print ("Scheduling event for 10 seconds time, current time=", now, "off time=", self.__turnOffTime) 
        else:
            # __pin already on... just increase timer delay
            self.__turnOffTime = self.__turnOffTime + datetime.timedelta(0, 10)
            delayUntilOff = self.__turnOffTime - datetime.datetime.utcnow()            
            self.__scheduler.cancel(self.__pinOffEventId)
            self.__pinOffEventId = self.__scheduler.enter(delayUntilOff.total_seconds(), 1, self.turnOff, ())
            
        self.__pin.on()
        
        print ("TimedPin.increaseTimeOn()")

    def turnOff(self):
        self.__pin.off()
        print ("TimedPin.turnOff()")
    
    def getStateStr(self):
        message = ""
        if self.__pin.getIsOn() == True:
            #__pin is on...
            N = self.__turnOffTime - datetime.datetime.utcnow() 
            message = "Pin is on, will Turn Off in " + str(N.total_seconds()) + " seconds (at: " + self.__turnOffTime.strftime("%A, %d. %B %Y %H:%M:%S") + ")"
        else:
            # __pin is off...
            message = "Pin is off " 
        return message
    
    def getTimeRemainingOn(self):
        timedelta = datetime.datetime.utcnow()-self.__turnOffTime
        timedeltaString = timedelta
        return timedeltaString 
        
    def startSchedulerThread(self):
        self.__threadObj = threading.Thread(target=self.startScheduler)
        self.__threadObj.start()
         
    def startScheduler(self): 
        print 'startScheduler(): Starting to run scheduler at ', time.time()
        self.__scheduler.run()
        print 'startScheduler(): FINISHED at ', time.time()
        