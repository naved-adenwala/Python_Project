#library
from tkinter import *
import calendar

wind = Tk()
wind.geometry("500x500")
#function to display calendar
def calendar_display():
    wind.title("Calendar")
    wind.config(background="grey")
    wind.geometry("525x650")
    year = int(inp.get())
    get_calendar = calendar.calendar(year)
    calyear = Label(wind,text=get_calendar,font=("timesnewroman",11,"bold"))
    calyear.grid(row=1,column=5)
    wind.mainloop()


#output
wind.config(background="black")
wind.title("Calendar")
cal = Label(wind,text="Enter Year to get calendar",bg="grey",font=("timesnewroman",10,"bold"))
cal.place(x=40,y=10)
inp = Entry(wind)
inp.place(x=60,y=40)
btn = Button(wind,text="Show Calander",bg="red",fg="white",command=calendar_display)
btn.place(x=75,y=70)


wind.mainloop()
