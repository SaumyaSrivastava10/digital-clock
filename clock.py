#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import *

from time import strftime

def time():
    string=strftime("%H:%M:%S %p")
    labe1.config(text=string)
    labe1.after(1000, time)
root=Tk()
root.title("Digital-Clock")
labe1=Label(root, font=("ds-digital",80),background="black",foreground="cyan")
labe1.pack(anchor="center")
time()

mainloop()
