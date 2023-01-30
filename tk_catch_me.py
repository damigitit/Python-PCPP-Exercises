"""
Author: Damian Archer
Date: 1/28/2023
File: tk_catch_me.py
Purpose: PCPP Exercises
"""

import tkinter as tk
from tkinter import Button
from tkinter import IntVar
import random
import secrets

def move(*args):
    if xval.get() < 250 and yval.get() < 250:
        xval.set(random.randrange(250,400))
        yval.set(random.randrange(100,250))
    else:
        xval.set(random.randrange(100,250))
        yval.set(random.randrange(250,400))
    button.place(x=xval.get(),y=yval.get())
    master.config(bg="#"+secrets.token_hex()[0:3])



master = tk.Tk()
master.geometry("500x500")

xval = IntVar()
yval = IntVar()

button = Button(master, text="Catch me!")
button.place(x=xval.get(),y=yval.get())
button.bind("<Enter>", move)

if __name__ == '__main__':
    master.mainloop()

