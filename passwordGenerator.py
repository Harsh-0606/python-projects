#importing files
import random
from  tkinter import *
import pyperclip

#making window 
root=Tk()
root.title("Password Generator")
root.geometry("500x150")
root.minsize(500,150)
root.resizable(True,True)

#setting the text font 
textFont=("Times New Roman", 40, "bold")
background="black"
foreground="white"
root['background']='black'
label= Label(root,font=textFont,bg=background,fg=foreground)
label.pack(expand=True)

#password generation logic
def passwordGenerator():
    passwordLength=15
    store="qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()?"
    p = "".join(random.sample(store,passwordLength))
    pyperclip.copy(p)
    spam = pyperclip.paste()
    label.config(text=p)

#close window logic
def closeWin(e):
    root.destroy()

#buttons and calling the mainloop()
root.bind('<Escape>',lambda e: closeWin(e))
buttonFont= ("Times New Roman", 10)
button = Button(root,text="Generate Password", command=passwordGenerator,pady=5,font=buttonFont,justify='center')
button.pack(expand=True)
passwordGenerator()
root.mainloop()

