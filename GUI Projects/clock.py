#importing libraries
import time
from tkinter import *
#screen setting
window = Tk()
window.geometry("360x120")
window.resizable(0,0)
window.title("Digital Clock")

#font and color
label= Label(window,bg="darkblue",fg="white",font="TimeNewRoman 24",bd=140)
label.pack()

#function to update time
def clock():

    tim = time.strftime("%H:%M:%S") #current time
    label.config(text=tim)
    label.after(1,clock) #upating time


clock()
window.mainloop()



