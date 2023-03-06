import tkinter as tk
from tkinter import * 
from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter import messagebox,filedialog
from tkinter import *
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL
import webbrowser



class Settings(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.focus_force()
        self.configure(bg='#303135')
        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()
        y=int((self.sh-500)/2)-30
        x=int((self.sw-500)/2)
        self.geometry('%dx%d+%d+%d' % (500, 500, x, y))
        self.title('Youtube-dl GUI  Settings')
        Label(self, text = "Settings",font=('Arial', 16),bg="#303135",fg="white").place(relx=0.5, rely=0.05,anchor= CENTER)
        Label(self, text = "Default Download Options",bg="#303135",fg="white").place(relx=0.5, rely=0.12,anchor= CENTER)
        Label(self, text = "Path to Cookie file",bg="#303135",fg="white").place(relx=0.5, rely=0.28,anchor= CENTER)
        Label(self, text = "Output template for video",bg="#303135",fg="white").place(relx=0.5, rely=0.44,anchor= CENTER)
        Label(self, text = "Output template for playlist",bg="#303135",fg="white").place(relx=0.5, rely=0.56,anchor= CENTER)
        Label(self, text = "Multi video options",bg="#303135",fg="white").place(relx=0.5, rely=0.7,anchor= CENTER)
        dd=Label(self, text = "Update  yt-dlp",fg="#0574FF",cursor="hand2",bg="#303135")
        dd.place(x = 390,y = 460)
        #dd.bind("<Button-1>", lambda e: updateback())
        name75 = Label(self, text = "Report issue",fg="#0574FF",cursor="hand2",bg="#303135")
        name75.place(x = 15,y = 460)
        name75.bind("<Button-1>", lambda e: webbrowser.open('https://github.com/sourabhkv/ytdl/issues'))
    
        ttk.Button(self, text ="Save", command = self.save).place(relx=0.5, rely=0.89,anchor= CENTER)
        file2=open("./database/cookies.txt",'r')
        data1=file2.readlines()
        file2.close()
        file3=open("./database/args.txt",'r')
        data2=file3.readlines()
        file3.close()
        file4=open("./database/output_temp_vid.txt",'r')
        out_temp_vid=file4.readlines()
        file4.close()
        file5=open("./database/output_temp_playlist.txt",'r')
        out_temp_plst=file5.readlines()
        file5.close()
        self.video=ttk.Combobox(self, width="20", values=["144p","240p","360p","480p","720","1080p"],state="readonly")
        file8=open("./database/multivideo.txt","r")
        
        r=file8.readlines()
        self.video.set(r[0][:-1])
        self.video.place(x=100,y=370)
        self.audio=ttk.Combobox(self, width="20", values=["ba","wa"],state="readonly")
        self.audio.set(r[-1])
        self.audio.place(x=270,y=370)
        file8.close()

        
        
        self.optnentry=ttk.Entry(self,width=74)
        self.cookiepath=ttk.Entry(self,width=71)
        self.out_vid=ttk.Entry(self,width=74)
        self.out_plst=ttk.Entry(self,width=74)
        
        if len(data2)!=0:
            self.optnentry.insert(0,data2[0])
        elif len(data1)!=0:
            self.cookiepath.insert(0,data1[0])
        
        self.out_plst.insert(0,out_temp_plst[0])
        self.out_plst.place(x=20,y=300)
        self.out_vid.insert(0,out_temp_vid[0])
        self.out_vid.place(x=20,y=240)
    
        self.optnentry.place(x=20,y=78)
    #cookiepath.insert(0,data3)
        self.cookiepath.place(x=20,y=158)
        Button(self, text =".", command = self.cookieselect).place(x=455,y=156)
        self.resizable(False, False)
        self.iconbitmap('./logo.ico')
        
    def cookieselect(self):
        r = filedialog.askopenfilename()
        self.cookiepath.delete(0,END)
        self.cookiepath.insert(0,r)
        self.focus_force()

    def save(self):
        c1=self.optnentry.get()
        c2=self.cookiepath.get()
        c3=self.out_vid.get()
        c4=self.out_plst.get()
        
        for i,j in {"./database/args.txt":c1,"./database/cookies.txt":c2,"./database/output_temp_vid.txt":c3,"./database/output_temp_playlist.txt":c4,"./database/multivideo.txt":self.video.get()+"\n"+self.audio.get()}.items():
            with open(i,"w+") as file:
                file.write(j)

        self.destroy()
        messagebox.showinfo("Youtube-dl GUI", "Settings saved!")