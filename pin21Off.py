import web
import setPin as setPin

      
class pin21Off:
    def GET(self):
        setPin.setGpioOutPinState(21, False)
        print ("pin 21 off received....")
        return web.template.render('templates/').welcome("pin 21 off received....");
