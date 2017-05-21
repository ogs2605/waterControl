import web
import setPin as setPin

class pin20On:
    def GET(self):
        setPin.setGpioOutPinState(20, True)
        print ("pin 20 on received....")
        return web.template.render('templates/').welcome("pin 20 on received....");
    


