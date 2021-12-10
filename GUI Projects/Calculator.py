from tkinter import *

#screen
win = Tk()
win.title("Calculator")
win.geometry("340x450")
win.config(bg="darkgrey")


#text
name = Label(win,text="Calculator",font=("Times",20,"bold"),bg="darkgrey").place(x=120,y=9)

#variables
text = StringVar()
operator = "" #u


def on_click(num):
    global operator
    operator = operator + num
    text.set(operator)

def calculation():
    global operator
    add =str(eval(operator))
    text.set(add)
    operator = ""


def clear():
    text.set("")


inp = Entry(win,font=("Times",12,"bold"),textvar=text,width=40,bd=5,bg="#a2af77").place(x=4,y=40)

but1=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:on_click("1"),text="1",font=("TimesNewRoman",16,'bold'))
but1.place(x=10,y=100)

but2=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:on_click("2"),text="2",font=("TimesNewRoman",16,'bold'))
but2.place(x=10,y=170)

but3=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:on_click("3"),text="3",font=("TimesNewRoman",16,'bold'))
but3.place(x=10,y=240)

but4=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:on_click("4"),text="4",font=("TimesNewRoman",16,'bold'))
but4.place(x=75,y=100)

but5=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:on_click("5"),text="5",font=("TimesNewRoman",16,'bold'))
but5.place(x=75,y=170)

but6=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:on_click("6"),text="6",font=("TimesNewRoman",16,'bold'))
but6.place(x=75,y=240)

but7=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:on_click("7"),text="7",font=("TimesNewRoman",16,'bold'))
but7.place(x=140,y=100)

but8=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:on_click("8"),text="8",font=("TimesNewRoman",16,'bold'))
but8.place(x=140,y=170)

but9=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:on_click("9"),text="9",font=("TimesNewRoman",16,'bold'))
but9.place(x=140,y=240)

but0=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:on_click("0"),text="0",font=("TimesNewRoman",16,'bold'))
but0.place(x=10,y=310)

but=Button(win,padx=14,pady=14,bd=4,bg='white',command=lambda:on_click("."),text=". ",font=("TimesNewRoman",16,'bold'))
but.place(x=75,y=310)

addition=Button(win,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:on_click("+"),font=("TimesNewRoman",16,'bold'))
addition.place(x=205,y=100)

sub=Button(win,padx=14,pady=14,bd=4,bg='white',text="- ",command=lambda:on_click("-"),font=("TimesNewRoman",16,'bold'))
sub.place(x=205,y=170)

div=Button(win,padx=14,pady=14,bd=4,bg='white',text="* ",command=lambda:on_click("*" ),font=("TimesNewRoman",16,'bold'))
div.place(x=205,y=240)

div=Button(win,padx=14,pady=14,bd=4,bg='white',text="/ ",command=lambda:on_click("/"),font=("TimesNewRoman",16,'bold'))
div.place(x=140,y=310)


butcalculation=Button(win,padx=125,pady=10,bd=4,bg='white',command=clear,text="Clear",font=("TimesNewRoman",16,'bold'))
butcalculation.place(x=9,y=380)

butclear=Button(win,padx=14,pady=119,bd=4,bg='white',text="=",command=calculation,font=("TimesNewRoman",16,'bold'))
butclear.place(x=270,y=100)

win.mainloop()
