from time import time
from tkinter import Tk, Label, Entry, PhotoImage, Button
from random import randint
from pygame import mixer
from os import name
# from multiprocessing import Process
ison=False
stopPlaying=True
total_time=1
def slepgui(timeforsleep):
    global root
    starttime = time()
    while True:
        if (starttime <= time()-timeforsleep):
            break
        else:
            root.update()
mixer.init()
colorfromosfortext = "#ffffff"
obg = "#31363b"
def checkosforgui():
    global colorfromosfortext, obg
    if name == "nt":
        obg = "#ffffff"
        colorfromosfortext="#000000"

def tap():
    r = randint(30, 240)
    setMetronomeValue(r)

def setMetronomeValue(value):
    speed_w.delete(0, "end")
    speed_w.insert("end",f"{value}")


def play():
    global stopPlaying, total_time
    play_w.config(image=pauseimg)
    while True:
        total_time= 60/int(speed_w.get())
        
        if stopPlaying == True:
            break
        else:
            mixer.music.load("beat1.wav")
            mixer.music.play()
            
            slepgui(total_time)
            
            mixer.music.load("beat2.wav")
            
            mixer.music.play()
            
            slepgui(total_time)
            
            mixer.music.play()
            
            slepgui(total_time)
            
            mixer.music.play()
            
            slepgui(total_time)
            

def pause():
    
    play_w.config(image=butimg)


def toggleButton():
    global ison, stopPlaying, total_time
    total_time= 60/int(speed_w.get())
    if (ison == False):
        ison = True
        stopPlaying=False

        play()
    else:
        ison=False
        stopPlaying=True
        pause()


root = Tk()
root.title("Pynome")
root.geometry("350x400")
root.resizable(0,0)
checkosforgui()
root.config(bg=f"{obg}")
root.iconphoto(False, PhotoImage(file='icon.png'))
curFont = "Source Code Pro"
butimg = PhotoImage(file=r"play.png")
tapimg = PhotoImage(file=r"tap.png")
pauseimg = PhotoImage(file=r"pause.png")
Label(text="PyNome", font=(f"{curFont}",20), bg=f"{obg}",fg=f"{colorfromosfortext}").pack(pady=10)
speed_w = Entry(font=(f"{curFont}",20), borderwidth=0, relief="flat", highlightthickness=0, bg=f"{obg}",fg=f"{colorfromosfortext}", justify="center")
speed_w.pack(pady=20)
speed_w.insert("end", "120")
tap_w = Button(image=tapimg, relief="flat", borderwidth=0, highlightthickness=0, command=tap, bg="#31363b")
lef=116
tap_w.place(x=lef, y=260)
play_w = Button(image=butimg, relief="flat", borderwidth=0, highlightthickness=0, command=toggleButton,bg="#31363b")
play_w.place(x=lef,y=320)
root.mainloop()
