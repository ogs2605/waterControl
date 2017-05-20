import web
import setPin as setPin

class pin21On:
    def GET(self):
        print ("NEW CLASS!")
        print ("pin 21 on received....")
        setPin.setGpioOutPinState(21, True)        
        return web.template.render('templates/').welcome("pin 21 on received....");
     
class EggieTest:
    def __init__(self):
        self.name="Eggie"
          
    def doNothing(self):
        print ("Naaaah")
        return
    