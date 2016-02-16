import web
from web import form
import os
import setPin as setPin

render = web.template.render('templates/')

login = form.Form(
    form.Textbox('username'),
    form.Password('password'),
    form.Button('Login1'),
    form.Button('Login2'),
    form.Button('Login3'),
)

# tuples of URL pattern and name of handler class 
urls = (
  '/', 'index', 
  '/pin21On', 'pin21On', 
  '/pin21Off', 'pin21Off', 
  '/pin20On', 'pin20On', 
  '/pin20Off', 'pin20Off', 
  "/users/(.+)", "list_users"
)

class pin21On:
    def GET(self):
      print "pin 21 on received...."
      setPin.setGpioOutPinState(21, True)        
      return "pin 21 on received...."
      
class pin21Off:
    def GET(self):
      setPin.setGpioOutPinState(21, False)
      print "pin 21 off received...."
      return "pin 21 off received...."

class pin20On:
    def GET(self):
      setPin.setGpioOutPinState(20, True)
      print "pin 20 on received...."
      return "pin 20 on received...."

class pin20Off:
    def GET(self):
      setPin.setGpioOutPinState(20, False)
      print "pin 20 off received...."
      return "pin 20 off received...."

class list_users:
    def GET(self, name):
        print "web.input()", format (web.input())
        print "name=", web.input()["name22"]
        return "Listing info about user: {0}".format(name), "name=", web.input()["name22"]

      
class index:
    def GET(self):
        form = login()
        return render.formtest(form)
        
    def POST(self):
        form = login()
        print form
        if not form.validates():
            return render.formtest(form)
        else:
            return os.system("python /home/pi/fivesecondOn.py"), "username", form['username'].value, "password", form['password'].value
                    
print urls

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    
