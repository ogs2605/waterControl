import web
from webserver import pin21

class pin21Off:
    def GET(self):
        pin21.off()
        return web.template.render('templates/').welcome("pin 21 off received....");