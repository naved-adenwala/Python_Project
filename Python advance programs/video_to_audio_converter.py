from tkinter.filedialog import askopenfilename
import os
import moviepy.editor
f = askopenfilename()
video = moviepy.editor.VideoFileClip(f)
audio = video.audio
aud_name = input("Name your audio file ")
ch = input("Enter path to save this file ")
os.chdir(ch)
audio.write_audiofile(f"{aud_name}.mp3")