from math import exp
import random
from  tkinter import *
from tkinter import font
import tkinter

root=Tk()
root.title("Password Generator")
root.geometry("500x150")
root.minsize(500,150)
root.resizable(True,True)

textFont=("Times New Roman", 40, "bold")
background="black"
foreground="white"
root['background']='black'
label= Label(root,font=textFont,bg=background,fg=foreground)
label.pack(expand=True)

def passwordGenerator():
    passwordLength=15
    store="qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()?"
    p = "".join(random.sample(store,passwordLength))
    label.config(text=p)
    # label.after(1,passwordGenerator)

def closeWin(e):
    root.destroy()

root.bind('<Escape>',lambda e: closeWin(e))
buttonFont= ("Times New Roman", 10)
button = tkinter.Button(root,text="Generate Password", command=passwordGenerator,pady=5,font=buttonFont,justify='center')
button.pack(expand=True)
passwordGenerator()
root.mainloop()