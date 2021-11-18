#importing libraries
from tkinter import Label, Tk 
import time

#creating the window, naming it and setting the size
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("450x150") 
app_window.resizable(1,1)

#definig the properties of label 
text_font= ("Times New Roman", 40)
background = "#000"
foreground= "#fff"
app_window['background']="black"
# it is where we place the text and images its equivalent to a division tag
label = Label(app_window, font=text_font, bg=background, fg=foreground) 
#pack() Method, This geometry manager organizes widgets in blocks before placing them in the parent widget.
label.pack(expand=True)

#clock logic/code
def digital_clock(): 
   time_live = time.strftime("%I:%M:%S %p")
   label.config(text=time_live) 
   label.after(100, digital_clock)

#cclose function
def close_win(e):
   app_window.destroy()

#logic to close with Esc key
app_window.bind('<Escape>', lambda e: close_win(e))

#calling clock logic
digital_clock()
#it is telling python to run the mainloop of tkinter
app_window.mainloop()