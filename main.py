import random
import smtplib
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty

class MyGridLayout(GridLayout):
    objname = ObjectProperty(None)
    objemail = ObjectProperty(None)
    objphone = ObjectProperty(None)
    objotp = ObjectProperty(None)
    authotp = ""


    def sendbtn(self):
        print(f"Name: {self.objname.text}")
        print(f"Email: {self.objemail.text}")
        print(f"Phone: {self.objphone.text}")
        # create smtp session

        s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
        # start TLS for E-mail security
        s.starttls()
        # Log in to your gmail account
        s.login("otpgeneratorpython@gmail.com", "otpgenerator")
        otp = random.randint(1000, 9999)
        otp = str(otp)
        self.authotp = otp

        s.sendmail("191210025@nitdelhi.ac.in", self.objemail.text , otp)
        self.objname.text = ""
        self.objemail.text = ""
        self.objphone.text = ""

        #close smtp session
        s.quit()
        print("OTP generated and sent successfully")

    def authbtn(self):
        if (self.objotp.text == self.authotp):
            self.objotp.text = ""
            print("\nAuthorized ")



class MyOTPApp(App):
    def build(self):
        Window.clearcolor = (0.6, 0.1, 0.2, 2)
        return MyGridLayout()

if __name__ == '__main__' :
    MyOTPApp=MyOTPApp()
    MyOTPApp.run()



