#libraries
import pygame
import tkinter as tk
#ask to select folder
from tkinter.filedialog import askdirectory
import os

musicplayer = tk.Tk()
musicplayer.title("Naved Music Player")
musicplayer.geometry("450x350")
directory = askdirectory()
#changing cirectory as per user selection
os.chdir(directory)
songs_list = os.listdir()
print(songs_list)

play_list = tk.Listbox(musicplayer,font="MonoLisa 20",bg="white",selectmode=tk.SINGLE)
for item in songs_list:
    pos = 0
    #setting position of songs list
    play_list.insert(pos,item)
    pos +=1
pygame.init()
pygame.mixer.init()


def play():
    #playing selected sound
    pygame.mixer.music.load(play_list.get(tk.ACTIVE))
    #setting into a variable
    var.set(play_list.get(tk.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

button1 = tk.Button(musicplayer,width=100,height=1,font="TimeNewRoman 20",text="PLAY",command=play,bg="Green",fg="black")
button2 = tk.Button(musicplayer,width=100,height=1,font="TimeNewRoman 20",text="Stop",command=stop,bg="red",fg="black")
button3 = tk.Button(musicplayer,width=100,height=1,font="TimeNewRoman 20",text="PAUSE",command=pause,bg="yellow",fg="black")
button4 = tk.Button(musicplayer,width=100,height=1,font="TimeNewRoman 20",text="UNPAUSE",command=unpause,bg="violet",fg="black")

button1.pack()
button2.pack()
button3.pack()
button4.pack()
play_list.pack(fill="both",expand="yes")


var = tk.StringVar()

musicplayer.mainloop()