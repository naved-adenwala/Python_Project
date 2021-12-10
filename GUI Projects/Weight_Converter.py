from tkinter import *
#setup
wind = Tk()
wind.title("Weight Converter")
wind.geometry("600x600")


#formula
# 1 ounce = 0.035274
# 1 gram = 1000 mg
# 1 pound = 0.00220462


#converter * 1000 for 1 kg
def convert_in_kg():
    gram = float(weight.get()) * 1000
    pound = float(weight.get()) * 2.20462
    ounce = float(weight.get()) * 35.274

    #inserting and deleting previous values
    c1.delete("1.0",END)
    c1.insert(END,gram)
    c2.delete("1.0", END)
    c2.insert(END, pound)
    c3.delete("1.0", END)
    c3.insert(END, ounce)

#variable
weight = StringVar()

#text
tex= Label(wind,text="Enter Weight In (KG) to Convert ")

#input
entr = Entry(wind,width=30,textvariable=weight)

#text
g = Label(wind,text="Gram",font=("TimeNewRoman,10,bold"))
p = Label(wind,text="Pound",font=("TimeNewRoman,10,bold"))
o = Label(wind,text="Ounce",font=("TimeNewRoman,10,bold"))

#converted values
c1 = Text(wind,height=5,width=20)
c2 = Text(wind,height=5,width=20)
c3 = Text(wind,height=5,width=20)



#button
btn = Button(wind,text="Convert",command=convert_in_kg)
#position
tex.grid(row=0, column=0)
entr.grid(row=0, column=1)
g.grid(row=1, column=0)
p.grid(row=1, column=1)
o.grid(row=1, column=2)
c1.grid(row=2, column=0)
c2.grid(row=2, column=1)
c3.grid(row=2, column=2)
btn.grid(row=0, column=2)
wind.mainloop()
