import web
from webserver import pin19

class pin19On:
         
    def GET(self):
        pin19.on()
        return web.template.render('templates/').welcome("pin 19 on received....");
