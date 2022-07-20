import tkinter as tk
from pytube import YouTube

def download(s):
    #global E1
    print(s)
    global E1
    string = E1.get()
    yt = YouTube(str(string))
    videos = yt.__getattribute__()
    s = 1
    for v in videos:
        print(str(s) + "." + str(v))
        s += 1
    n = int(input("Enter you choice of video quality\n>>"))
    vid = videos[n - 1]
    dest = str(input("Enter you destination path\n>>"))
    vid.download(dest)
    print(YouTube.views + "video has been downloaded")

root = tk.Tk()
w = tk.Label(text="Youtube Downloader")
w.pack()

E1 = tk.Entry(bd=5)
E1.bind("<Return>", (lambda event: download(E1.get())))
E1.pack(side=tk.TOP)

button = tk.Button(text="Download", fg="red", command=lambda: download(E1.get()))
button.pack(side="bottom")


root.mainloop()

