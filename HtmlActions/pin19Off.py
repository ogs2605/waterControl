import setPin as setPin
import web

class pin19Off:
    def GET(self):
        setPin.setGpioOutPinState(19,False)
        print ("pin 19 off received....")
        return web.template.render('templates/').welcome("pin 19 off received....");