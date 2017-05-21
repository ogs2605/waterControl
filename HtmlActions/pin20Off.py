import web
from webserver import pin20

class pin20Off:
    def GET(self):
        pin20.off()
        return web.template.render('templates/').welcome("pin 20 off received....");