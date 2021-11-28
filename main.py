import random
import smtplib
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty



# create smtp session
#s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
# start TLS for E-mail security
#s.starttls()
# Log in to your gmail account
#s.login("191210025@nitdelhi.ac.in", "jeremyjosephabraham")
#otp = random.randint(1000, 9999)
#otp = str(otp)

#s.sendmail("191210025@nitdelhi.ac.in", "staticronaldo@gmail.com", otp)

#close smtp session
#s.quit()

class MyGridLayout(GridLayout):
    objname = ObjectProperty(None)
    objemail = ObjectProperty(None)
    objphone = ObjectProperty(None)

    def btn(self):
        print(f"Name: {self.objname.text}")
        print(f"Email: {self.objemail.text}")
        print(f"Phone: {self.objname.text}")
        print("OTP Generated and sent successfully")











class MyOTPApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__' :
    MyOTPApp=MyOTPApp()
    MyOTPApp.run()



