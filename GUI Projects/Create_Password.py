#module
from tkinter import *
import random,string,pyperclip

#basic setup
window = Tk()
window.geometry("350x350")
window.title("Password Generator")
#variable
name_of_pass = StringVar()
#output
label = Label(window,text="Enter Your Name",font="TimesNewRoman 10").place(x=90,y=11)
#input
name = Entry(window, textvariable=name_of_pass).place(x=110, y=40)

#second variable
stri = StringVar()

#function to generate password
def passwordgenerator():
    password = name_of_pass.get() + random.choice(string.digits)+random.choice(string.ascii_lowercase)+random.choice(string.punctuation)+random.choice(string.ascii_uppercase)
    stri.set(password)

#on press it will generate password
butt = Button(window,text="Generate Password",command=passwordgenerator).place(x=115,y=72)
#it will added to another input box
dis = Entry(window,textvariable=stri).place(x=110,y=110)

#copy function
def copy():
    pyperclip.copy(stri.get())

#on pressing the button it will copy that password
butt2 = Button(window,text="Copy",command=copy).place(x=140,y=150)
window.mainloop()


