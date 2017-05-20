import setPin as setPin
import web

class pin19On: 
    def GET(self):
        setPin.setGpioOutPinState(19,True)
        print ("pin 19 on received....")
        return web.template.render('templates/').welcome("pin 19 on received....");