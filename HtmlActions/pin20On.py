import web
from webserver import pin20

class pin20On:
         
    def GET(self):
        pin20.off()
        return web.template.render('templates/').welcome("pin 20 off received....");
