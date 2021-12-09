#importing module
from tkinter import filedialog
import tkinter as tk
from PIL import Image

#screen
window = tk.Tk()
window.title("Image Converter")
#background setting
canvas = tk.Canvas(window,height=400,width=400,bg="#c9ebf2") #,relief="raised"
canvas.pack()
#text
label = tk.Label(window,text="Image Converter",font="TimesNewRoman",fg="black",bg="#c9ebf2").place(x=158,y=30)

#function to ask directory
def file():
    global img
    file_name = filedialog.askopenfilename()
    img = Image.open(file_name) #get name

#button
btn = tk.Button(window,text="Select Your File",command=file,fg='white', font=('helvetica', 12, 'bold'),bg="#074f5e")
btn.place(x=150,y=60)

def convert():
    global img
    save_file = filedialog.asksaveasfilename(defaultextension=".jpg") #save
    img.save(save_file)#image converter

#button
btn2 =tk.Button(window,text="Convert",command=convert,fg='white', font=('helvetica', 12, 'bold'),bg="#074f5e")
btn2.place(x=175,y=100)

window.mainloop()