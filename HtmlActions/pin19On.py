import web
from webserver import pin19

class pin19On:
         
    def GET(self):
        pin19.off()
        pin19.startSchedulerThread()
        return web.template.render('templates/').welcome("pin 19 off received....");
