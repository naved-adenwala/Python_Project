from tkinter import *
from pytube import YouTube

window = Tk()
window.geometry('800x300')
window.resizable(0,0)
window.title("YouTube Downloader")

video_url = StringVar()

Label(window,text = 'YouTube Video Downloader', font ='TimeNewRomen 20').pack()
Label(window, text = 'URL:', font = 'TimeNewRomen 25 bold').place(x= 10 , y = 60)
url_field = Entry(window, width = 65, textvariable = video_url).place(x= 100, y = 80)

def down():
    url = YouTube(video_url.get())
    video = url.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download()



Button(window, text = "Download", font = 'arial 14 bold', bg='#b3d9ff', border = 2, command = down).place(x=280, y=120)
window.mainloop()