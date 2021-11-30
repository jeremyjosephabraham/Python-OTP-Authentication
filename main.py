import random
import smtplib
import kivy_deps
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
Window.size = (400, 400)

class MyGridLayout(GridLayout):
    objname = ObjectProperty(None) #name passed from the text field
    objemail = ObjectProperty(None) #email passed from the text field
    objphone = ObjectProperty(None) #phone number passed from the text field
    objotp = ObjectProperty(None) #OTP entered by the user passed from the text field
    authotp = "0"


    def sendbtn(self):

        if (self.objemail.text != ""):
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
            otp = str(otp) #generated otp
            self.authotp = otp

            s.sendmail("otpgeneratorpython@gmail.com", self.objemail.text , otp) # sending the mail


            #close smtp session
            s.quit()
            print("OTP generated and sent successfully")
        else :
            print("Enter an email in the email field")





    def authbtn(self):
        if (self.objotp.text == self.authotp):

            self.objotp.text = ""
            self.objname.text = ""
            self.objemail.text = ""
            self.objphone.text = ""
            print("\nUser Authorized ")
        elif (self.authotp == ""):
            print("Generate the OTP first")
        else :
            print("OTP is incorrect")
            print("Unauthorized")



class MyOTPApp(App):
    def build(self):
        Window.clearcolor = (0.804, 0.361, 0.361,1)
        return MyGridLayout()

if __name__ == "__main__" :
    MyOTPApp=MyOTPApp()
    MyOTPApp.run()



