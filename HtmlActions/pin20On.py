import web
from webserver import pin20

class pin20On:
         
    def GET(self):
        pin20.on()
        return web.template.render('templates/').welcome("pin 20 on received....");
