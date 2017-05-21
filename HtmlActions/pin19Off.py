import web
from webserver import pin19

class pin19Off:
         
    def GET(self):
        pin19.off()
        return web.template.render('templates/').welcome("pin 19 off received....");
