import setPin as setPin
import web

class pin20Off:
    def GET(self):
        setPin.setGpioOutPinState(20, False)
        print ("pin 20 off received....")
        return web.template.render('templates/').welcome("pin 20 off received....");
