import web
from web import form
import os
import setPin as setPin
import HtmlActions
from Pin import Pin


render = web.template.render('templates/')
pin19 = Pin(19)
pin20 = Pin(20)
pin21 = Pin(21) 

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

class allPinsOff:
    def GET(self):
        setPin.setGpioOutPinState(19,False)
        setPin.setGpioOutPinState(20,False)
        setPin.setGpioOutPinState(21,False)
        print ("All Pins Off received....")
        return render.welcome("All Pins Off received...");

class livingAreaLightsOn:
    def GET(self):
        print ("Turning Living Area Lights On...")
        print ("Sending groupswrite ip:localhost 0/0/3 0x01")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 0/0/3 0x01")
        return render.welcome("Turning Living Area Lights On...");

class livingAreaLightsOff:
    def GET(self):
        print ("Turning Living Area Lights Off...")
        print ("Sending groupswrite ip:localhost 0/0/3 0x00")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 0/0/3 0x00")
        return render.welcome("Turning Living Area Lights Off...");

class diningAreaLightsOn:
    def GET(self):
        print ("Turning Dining Area Lights On...")
        print ("Sending groupswrite ip:localhost 0/0/1 0x01")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 0/0/1 0x01")
        return render.welcome("Turning Dining Area Lights On...");

class diningAreaLightsOff:
    def GET(self):
        print ("Turning Dining Area Lights Off...")
        print ("Sending groupswrite ip:localhost 0/0/1 0x00")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 0/0/1 0x00")
        return render.welcome("Turning Dining Area Lights Off...");

class kitchenAreaLightsOn:
    def GET(self):
        print ("Turning Kitchen Area Lights On...")
        print ("Sending groupswrite ip:localhost 0/0/7 0x01")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 0/0/7 0x01")
        return render.welcome("Turning Kitchen Area Lights On...");

class kitchenAreaLightsOff:
    def GET(self):
        print ("Turning Kitchn Area Lights Off...")
        print ("Sending groupswrite ip:localhost 0/0/7 0x00")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 0/0/7 0x00")
        return render.welcome("Turning Kitchen Area Lights Off...");

class blindsUp:
    def GET(self):
        print ("Raising Blinds...")
        print ("Sending groupswrite ip:localhost 1/0/1 0x01")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 1/0/1 0x01")
        return render.welcome("Raising Blinds...");

class blindsDown:
    def GET(self):
        print ("Lowering Blinds...")
        print ("Sending groupswrite ip:localhost 1/0/0 0x01")
        os.system("/usr/local/bin/knxtool groupswrite ip:localhost 1/0/0 0x01")
        return render.welcome("Lowering Blinds...");


class list_users:
    def GET(self, name):
        print ("web.input()", format (web.input()))
        print ("name=", web.input()["name22"])
        return "Listing info about user: {0}".format(name), "name=", web.input()["name22"]

class index:
    def GET(self):
        return render.welcome("Welcome to the Raspberry Pi Controller for Watering and Blinds!!!!!")
        
    def POST(self):
        form = login()
        print (form)
        if not form.validates():
            return render.formtest(form)
        else:
            return os.system("python /home/pi/fivesecondOn.py"), "username", form['username'].value, "password", form['password'].value
                    
print (urls)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    
