import web
from web import form
import os
from Pin import Pin
from TimedPin import TimedPin
import datetime
import logging

render = web.template.render('templates/')

class WateringSystem (object):
    def __init__(self):
        print Pin
        self.pin19 = TimedPin(19)
        self.pin20 = TimedPin(20) 
        self.pin21 = TimedPin(21) 
    
    def getCurrentTimeStr(self):
        return datetime.datetime.utcnow().strftime("%A, %d. %B %Y %H:%M:%S")

wateringSystem = WateringSystem()

login = form.Form(form.Textbox('username'), form.Password('password'), form.Button('Login1'), form.Button('Login2'), form.Button('Login3'),)


# tuples of URL pattern and name of handler class 
urls = (
  '/', 'index', 
  '/pin21On', 'pin21On', 
  '/pin21Off', 'pin21Off', 
  '/pin20On', 'pin20On', 
  '/pin20Off', 'pin20Off', 
  '/pin19On', 'pin19On', 
  '/pin19Off', 'pin19Off',
  '/allPinsOff', 'allPinsOff',
  '/livingAreaLightsOn', 'livingAreaLightsOn',
  '/livingAreaLightsOff', 'livingAreaLightsOff', 
  '/diningAreaLightsOn', 'diningAreaLightsOn',
  '/diningAreaLightsOff', 'diningAreaLightsOff', 
  '/kitchenAreaLightsOn', 'kitchenAreaLightsOn',
  '/kitchenAreaLightsOff', 'kitchenAreaLightsOff', 
  '/blindsUp', 'blindsUp',
  '/blindsDown', 'blindsDown', 
  "/users/(.+)", "list_users"
)

class pin19On:
    def GET(self):
        wateringSystem.pin19.increaseTimeOn()
        #return web.template.render('templates/').welcome("pin 19 on received....", wateringSystem);
        return web.seeother("/")
    
class pin19Off:
    def GET(self):
        wateringSystem.pin19.turnOff()
        return web.seeother("/")
#       return web.template.render('templates/').welcome("pin 19 off received....", wateringSystem);

class pin20On:
    def GET(self):
        wateringSystem.pin20.increaseTimeOn()
        return web.seeother("/")
#        return web.template.render('templates/').welcome("pin 20 on received....", wateringSystem);

class pin20Off:
    def GET(self):
        wateringSystem.pin20.turnOff()
        return web.seeother("/")
#        return web.template.render('templates/').welcome("pin 20 off received....", wateringSystem);
    
class pin21On:
    def GET(self):
        wateringSystem.pin21.increaseTimeOn()
        return web.seeother("/")
#        return web.template.render('templates/').welcome("pin 21 on received....", wateringSystem);

class pin21Off:
    def GET(self):
        wateringSystem.pin21.turnOff()
        return web.seeother("/")
#        return web.template.render('templates/').welcome("pin 21 off received....", wateringSystem);

class allPinsOff:
    def GET(self):
        wateringSystem.pin19.turnOff()
        wateringSystem.pin20.turnOff()
        wateringSystem.pin21.turnOff()
        return web.seeother("/")
#        print ("All Pins Off received....")
        return render.welcome("All Pins Off received...", wateringSystem);

class livingAreaLightsOn:
    def GET(self):
        print ("Turning Living Area Lights On...")
        print ("Sending groupswrite ip:localhost 0/0/3 0x01")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 0/0/3 0x01")
        return render.welcome("Turning Living Area Lights On...", wateringSystem);

class livingAreaLightsOff:
    def GET(self):
        print ("Turning Living Area Lights Off...")
        print ("Sending groupswrite ip:localhost 0/0/3 0x00")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 0/0/3 0x00")
        return render.welcome("Turning Living Area Lights Off...", wateringSystem);

class diningAreaLightsOn:
    def GET(self):
        print ("Turning Dining Area Lights On...")
        print ("Sending groupswrite ip:localhost 0/0/1 0x01")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 0/0/1 0x01")
        return render.welcome("Turning Dining Area Lights On...", wateringSystem);

class diningAreaLightsOff:
    def GET(self):
        print ("Turning Dining Area Lights Off...")
        print ("Sending groupswrite ip:localhost 0/0/1 0x00")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 0/0/1 0x00")
        return render.welcome("Turning Dining Area Lights Off...", wateringSystem);

class kitchenAreaLightsOn:
    def GET(self):
        print ("Turning Kitchen Area Lights On...")
        print ("Sending groupswrite ip:localhost 0/0/7 0x01")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 0/0/7 0x01")
        return render.welcome("Turning Kitchen Area Lights On...", wateringSystem);

class kitchenAreaLightsOff:
    def GET(self):
        print ("Turning Kitchn Area Lights Off...")
        print ("Sending groupswrite ip:localhost 0/0/7 0x00")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 0/0/7 0x00")
        return render.welcome("Turning Kitchen Area Lights Off...", wateringSystem);

class blindsUp:
    def GET(self):
        print ("Raising Blinds...")
        print ("Sending groupswrite ip:localhost 1/0/1 0x01")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 1/0/1 0x01")
        return render.welcome("Raising Blinds...", wateringSystem);

class blindsDown:
    def GET(self):
        print ("Lowering Blinds...")
        print ("Sending groupswrite ip:localhost 1/0/0 0x01")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 1/0/0 0x01")
        return render.welcome("Lowering Blinds...", wateringSystem);


class list_users:
    def GET(self, name):
        print ("web.input()", format (web.input()))
        print ("name=", web.input()["name22"])
        return "Listing info about user: {0}".format(name), "name=", web.input()["name22"]

class index:
    def GET(self):
        return render.welcome("Welcome to the Raspberry Pi Controller for Watering and Blinds!!!!!", wateringSystem)
        
    def POST(self):
        form = login()
        print (form)
        if not form.validates():
            return render.formtest(form)
        else:
            return os.system("python /home/pi/fivesecondOn.py"), "username", form['username'].value, "password", form['password'].value

if __name__ == "__main__":
    logging.warning("Watch OUt!")
    app = web.application(urls, globals())
    print (urls)
    app.run()
    
