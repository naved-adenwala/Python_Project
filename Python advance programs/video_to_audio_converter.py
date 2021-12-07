#module
from tkinter.filedialog import askopenfilename
import os
import moviepy.editor
#ask file name
f = askopenfilename()
#video file name
video = moviepy.editor.VideoFileClip(f) 
#video to audio
audio = video.audio
#file name
aud_name = input("Name your audio file ")
#file path
ch = input("Enter path to save this file ")
os.chdir(ch)
#output
audio.write_audiofile(f"{aud_name}.mp3")
