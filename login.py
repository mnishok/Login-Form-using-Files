import re
from tkinter import *
from PIL import Image, ImageTk

class Dashboard:
    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("750x500")
        self.frame.configure(bg='#f0f0f0')
        self.frame.title("Nishok M - Login Form Assignment")
        image = Image.open("guvi1.png")
        resize_image = image.resize((300, 125))
        photo = ImageTk.PhotoImage(resize_image)
        Label(self.frame, image=photo).pack()
        Label(self.frame, bg="#f0f0f0", text="Welcome!!!", font=("Arial", 35)).pack(pady=15)

        register = Button(self.frame, bg="#32ba51", text = "Register", fg="white", font=("sans-serif", 17), padx=10, pady=5, command = self.registerClick)
        register.place(x=150,y=250)
        login = Button(self.frame, bg="#32ba51", text = "Login", fg="white", font=("sans-serif", 17), padx=30, pady=4, command = self.loginClick)
        login.place(x=465,y=250)
        frgt_pwrd = Button(self.frame, bg="#32ba51", text = "Forget Password?", fg="white", font=("sans-serif", 17), padx=10, pady=5, command = self.frgt_pwrdClick)
        frgt_pwrd.place(x=258,y=350)

        self.frame.mainloop()

    def registerClick(self):
        self.frame.destroy()
        RegistrationPage()

    def loginClick(self):
        self.frame.destroy()
        LoginPage()

    def frgt_pwrdClick(self):
        self.frame.destroy()
        Frgt_pwrdPage()

class RegistrationPage:
    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("750x500")
        self.frame.configure(bg='#f0f0f0')
        self.frame.title("Nishok M - Login Form Assignment")
        Label(self.frame, bg="#f0f0f0", text="Registration Page", font=("Arial", 35)).pack(pady=50)

        Label(self.frame, anchor = "w", bg="#f0f0f0", fg="grey", text = "Email Address", font = ("Verdana", 11)).place(x=210,y=165)
        self.uname = StringVar()
        Entry(self.frame, textvariable=self.uname, font=("sans-serif", 17), width=25).place(x=210,y=195)
        Label(self.frame, anchor = "w", bg="#f0f0f0", fg="grey", text = "Password", font = ("Verdana", 11), width = 36).place(x=210,y=250)
        self.pword = StringVar()
        Entry(self.frame, textvariable=self.pword, font=("sans-serif", 17), show="*", width=25).place(x=210,y=280)

        Button(self.frame, bg="#32ba51", text = "Register", fg="white", font=("sans-serif", 15), padx=10,pady=5, command = self.onClick).place(x=323,y=360)

        self.frame.mainloop()

    def onClick(self):
        if self.emailValidation(self.uname.get()) and self.pwordValidation(self.pword.get()):
            self.f = open('credentials.txt','a')
            self.f.write(self.uname.get()+' '+self.pword.get()+'\n')
            self.f.close()
            self.frame.destroy()
            LoggedInPage()
        else:
            self.frame.destroy()
            InvalidMsgPage()

    def emailValidation(self, email):
        if re.fullmatch(r'\b[a-z0-9_]+@[a-z0-9]+\.[a-z]{2,3}\b', email):
            return True
        else:
            return False

    def pwordValidation(self, pword):
        self.regex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,15}$'
        if re.fullmatch(re.compile(self.regex), pword):
            return True
        else:
            return False

class InvalidMsgPage:
    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("750x500")
        self.frame.configure(bg='#f0f0f0')
        self.frame.title("Nishok M - Login Form Assignment")
        Label(self.frame, bg="#f0f0f0", text="Invalid Email or Password!", font=("Arial", 35)).pack(pady=50)
        self.msg = 'Your email should be a valid one\nand your password must contain a uppercase,\na lowercase, a digit, a special symbol and of length\n6-15 characters.'
        Label(self.frame, bg="#f0f0f0", text=self.msg, font=("Arial", 20)).pack(pady=30)

        register = Button(self.frame, bg="#32ba51", text = "Register", fg="white", font=("sans-serif", 17), padx=27, pady=5, command = self.registerClick)
        register.place(x=170,y=360)
        login = Button(self.frame, bg="#32ba51", text = "Dashboard", fg="white", font=("sans-serif", 17), padx=10, pady=5, command = self.backClick)
        login.place(x=422,y=360)

    def registerClick(self):
        self.frame.destroy()
        RegistrationPage()

    def backClick(self):
        self.frame.destroy()
        Dashboard()

class LoginPage:
    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("750x500")
        self.frame.configure(bg='#f0f0f0')
        self.frame.title("Nishok M - Login Form Assignment")
        Label(self.frame, bg="#f0f0f0", text="Login Page", font=("Arial", 35)).pack(pady=40)

        Label(self.frame, anchor = "w", bg="#f0f0f0", fg="grey", text = "Email Address", font = ("Verdana", 11)).place(x=210,y=155)
        self.uname = StringVar()
        Entry(self.frame, textvariable=self.uname, font=("sans-serif", 17), width=25).place(x=210,y=185)
        Label(self.frame, anchor = "w", bg="#f0f0f0", fg="grey", text = "Password", font = ("Verdana", 11), width = 36).place(x=210,y=230)
        self.pword = StringVar()
        Entry(self.frame, textvariable=self.pword, font=("sans-serif", 17), show="*", width=25).place(x=210,y=260)

        Button(self.frame, bg="#32ba51", text = "Login", fg="white", font=("sans-serif", 15), padx=8,pady=3, command = self.onClick).place(x=323,y=320)
        Button(self.frame, bg="#32ba51", text = "Go to Dashboard", fg="white", font=("sans-serif", 15), padx=7,pady=5, command = self.backClick).place(x=268,y=400)

        self.frame.mainloop()

    def onClick(self):
        if self.validCredentials():
            self.frame.destroy()
            LoggedInPage()
        else:
            self.frame.destroy()
            MismatchPage()

    def backClick(self):
        self.frame.destroy()
        Dashboard()

    def validCredentials(self):
        self.f = open('credentials.txt', 'r')
        for line in self.f:
            f_email, f_pword = line.split()
            if f_email == self.uname.get() and f_pword == self.pword.get():
                self.f.close()
                return True
        self.f.close()
        return False

class MismatchPage:
    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("750x500")
        self.frame.configure(bg='#f0f0f0')
        self.frame.title("Nishok M - Login Form Assignment")
        Label(self.frame, bg="#f0f0f0", text="No Matches Found!!", font=("Arial", 35)).pack(pady=115)
        Button(self.frame, bg="#32ba51", text = "Dashboard", fg="white", font=("sans-serif", 20), padx=10,pady=5, command = self.onClick).pack()

    def onClick(self):
        self.frame.destroy()
        Dashboard()

class Frgt_pwrdPage:
    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("750x500")
        self.frame.configure(bg='#f0f0f0')
        self.frame.title("Nishok M - Login Form Assignment")
        Label(self.frame, bg="#f0f0f0", text="Find your Password here!", font=("Arial", 35)).pack(pady=65)

        Label(self.frame, anchor = "w", bg="#f0f0f0", fg="grey", text = "Email Address", font = ("Verdana", 13)).place(x=210,y=180)
        self.uname = StringVar()
        Entry(self.frame, textvariable=self.uname, font=("sans-serif", 17), width=25).place(x=210,y=210)

        Button(self.frame, bg="#32ba51", text = "Find Password", fg="white", font=("sans-serif", 14), padx=7,pady=2, command = self.onClick).place(x=290,y=290)

    def onClick(self):
        self.pword = self.findPassword()
        if self.pword != -1:
            self.frame.destroy()
            ShowPassword(self.pword)
        else:
            self.frame.destroy()
            MismatchPage()

    def findPassword(self):
        self.f = open('credentials.txt', 'r')
        for line in self.f:
            f_email, f_pword = line.split()
            if f_email == self.uname.get():
                self.f.close()
                return f_pword
        self.f.close()
        return -1

class ShowPassword:
    def __init__(self, pword):
        self.frame = Tk()
        self.pword = pword
        self.frame.geometry("750x500")
        self.frame.configure(bg='#f0f0f0')
        self.frame.title("Nishok M - Login Form Assignment")
        Label(self.frame, bg="#f0f0f0", text="Your Password is,\n"+self.pword, font=("Arial", 35)).pack(pady=75)

        Button(self.frame, bg="#32ba51", text = "Login", fg="white", font=("sans-serif", 15), padx=8,pady=3, command = self.loginClick).place(x=323,y=280)
        Button(self.frame, bg="#32ba51", text = "Go to Dashboard", fg="white", font=("sans-serif", 15), padx=7,pady=5, command = self.backClick).place(x=268,y=375)

    def loginClick(self):
        self.frame.destroy()
        LoginPage()

    def backClick(self):
        self.frame.destroy()
        Dashboard()

class LoggedInPage:
    def __init__(self):
        self.frame = Tk()
        self.frame.geometry("750x500")
        self.frame.configure(bg='#f0f0f0')
        self.frame.title("Nishok M - Login Form Assignment")
        Label(self.frame, bg="#f0f0f0", text="Welcome!\n\nYou have successfully logged in!", font=("Arial", 35)).pack(pady=50)
        Button(self.frame, bg="#32ba51", text = "Logout", fg="white", font=("sans-serif", 20), padx=10,pady=5, command = self.onClick).place(x=323,y=320)
    def onClick(self):
        self.frame.destroy()
        LoginPage()

Dashboard()
