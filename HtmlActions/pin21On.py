import web
from webserver import pin21

class pin21On:
         
    def GET(self):
        pin21.on()
        return web.template.render('templates/').welcome("pin 21 on received....");

     
class EggieTest:
    def __init__(self):
        self.name="Eggie"
          
    def doNothing(self):
        print ("Naaaah")
        return
    