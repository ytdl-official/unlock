import tkinter as tk
from tkinter import * 
from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.constants import DISABLED, NORMAL
import webbrowser,os

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.focus_force()
        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()
        y=int((self.sh-500)/2)-30
        x=int((self.sw-600)/2)
        self.geometry('%dx%d+%d+%d' % (600, 500, x, y))
        self.title('About Youtube-dl GUI')
        self.configure(bg='#303135')
        self.image = Image.open("./images/logo.png")
        self.resize_image = self.image.resize((200, 200))
        self.img = ImageTk.PhotoImage(self.resize_image)
        streams = tk.Label(master=self, text = "",image=self.img,bg="#303135",font=('Arial', 16),fg="white").place(relx=0.5, rely=0.25,anchor= CENTER)
        streams2 = Label(self, text = "Youtube-dl GUI  v22.1002.19",bg="#303135",font=('Arial', 12),fg="white").place(relx=.5, rely=.5,anchor= CENTER)
        streams2 = Label(self, text = "Released under MIT License",bg="#303135",fg="white").place(relx=.5, rely=.56,anchor= CENTER)
        streams2 = Label(self, text = "This is project is based on yt-dlp , ffmpeg , atomic parsley",bg="#303135",fg="white").place(relx=.5, rely=.69,anchor= CENTER)
        streams3 = Label(self, text = "THIS IS ONLY FOR EDUCATIONAL PURPOSE.",font=('Arial', 9,'bold'),fg="red",bg="#303135").place(relx=.5, rely=.75,anchor= CENTER)
        name74 = Label(self, text = "CREDITS :",bg="#303135",fg="white").place(x=40+70,y=290)
        name74 = Label(self, text = "yt-dlp",bg="#303135",fg="#0574FF",cursor="hand2")
        name74.place(x = 135+85,y = 290)
        name74.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/yt-dlp/yt-dlp'))
        name73 = Label(self, text = "ffmpeg",fg="#0574FF",cursor="hand2",bg="#303135")
        name73.place(x = 210+95,y = 290)
        name73.bind("<Button-1>", lambda e: webbrowser.open('https://www.ffmpeg.org/'))
        name75 = Label(self, text = "AtomicParsley",fg="#0574FF",cursor="hand2",bg="#303135")
        name75.place(x = 290+105,y = 290)
        name75.bind("<Button-1>", lambda e: webbrowser.open('http://atomicparsley.sourceforge.net/'))
        name76 = Label(self, text = "TELEGRAM",fg="orange",cursor="hand2",bg="#303135")
        name76.place(x = 190+145,y = 390)
        name76.bind("<Button-1>", lambda e: webbrowser.open('https://t.me/ytdlgui'))
        name77 = Label(self, text = "DONATE",fg="yellow",cursor="hand2",bg="#303135")
        name77.place(x = 190,y = 390)
        name77.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/sourabhkv/ytdl#support-us'))
        name7e = Label(self, text = "Changelog",fg="#0574FF",cursor="hand2",bg="#303135")
        name7e.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/sourabhkv/ytdl/releases/tag/v22.0808.19'))
        name7e.place(x = 195,y = 315)
        name8e = Label(self, text = "Check for updates",fg="#0574FF",cursor="hand2",bg="#303135")
        name8e.bind("<Button-1>", lambda e: os.startfile("updater.exe"))
        name8e.place(x = 295,y = 315)
        streams2 = Label(self, text = "https://github.com/sourabhkv/ytdl",bg="#303135",fg="white").place(relx=.5, rely=.87,anchor= CENTER)
        streams2 = Label(self, text = "Developed by sourabhkv",bg="#303135",fg="green").place(relx=.5, rely=.93,anchor= CENTER)
        self.resizable(False, False)
        self.iconbitmap('./logo.ico')