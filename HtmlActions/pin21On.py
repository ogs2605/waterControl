import web
from webserver import pin21

class pin21On:
         
    def GET(self):
        pin21.off()
        return web.template.render('templates/').welcome("pin 21 off received....");

     
class EggieTest:
    def __init__(self):
        self.name="Eggie"
          
    def doNothing(self):
        print ("Naaaah")
        return
    