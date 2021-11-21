#importing libraries
from math import exp
import random
from tkinter import *

#making the window 
root=Tk()
root.title("Rock, Paper or Scrissors")
root.geometry('500x280')
root.resizable(0,0)

#setting font for label text
textFont=("Times New Roman", 40, "bold")
ScoreFont=("Times New Roman", 15, "bold")
background="black"
foreground="white"
root['background']='black'

#making labels 
labelcpu= Label(root,font=textFont,bg=background,fg=foreground)
labelcpu.place(x=50,y=50)

labelplayer= Label(root,font=textFont,bg=background,fg=foreground)
labelplayer.place(x=250,y=50)

labelround= Label(root,font=ScoreFont,bg=background,fg=foreground)
labelround.place(x=230,y=150,anchor="center")

#initializing game variables 
cpuScore = [0]
playerScore = [0]
choices = ["Rock", "Paper", "Scissors"]

#game logic
def RPS(player):
    computer = random.choice(choices)
    if player == computer:
        #change
        score="TIE!"
        labelround.config(text=score,fg="yellow")
    elif player == "Rock":
        if computer == "Paper":
            score="You lose! "+ computer+ " covers "+player
            labelround.config(text=score,fg="red")
            cpuScore[0]+=1
        else:
            score= "You win! "+ player+ " smashes "+ computer 
            labelround.config(text=score,fg="green")
            playerScore[0]+=1
    elif player == "Paper":
        if computer == "Scissors":
            score= "You lose! "+ computer+ " cut "+ player 
            labelround.config(text=score,fg="red")
            cpuScore[0]+=1
        else:
            score= "You win! "+ player+ " covers "+ computer 
            labelround.config(text=score,fg="green")
            playerScore[0]+=1
    elif player == "Scissors":
        if computer == "Rock":
            score= "You lose... "+ computer+ " smashes "+ player 
            labelround.config(text=score,fg="red")
            cpuScore[0]+=1
        else:
            score= "You win! "+ player+ " cut "+ computer 
            labelround.config(text=score,fg="green")
            playerScore[0]+=1

    cpu=f"CPU:{cpuScore[0]}"
    labelcpu.config(text=cpu)
    p=f"Player:{playerScore[0]}"
    labelplayer.config(text=p)

#close logic
def closeWin(e):
    root.destroy()

#reset game logic
def resetgame():
    cpuScore[0]=0
    playerScore[0]=0
    cpu=f"CPU:{cpuScore[0]}"
    labelcpu.config(text=cpu)
    p=f"Player:{playerScore[0]}"
    labelplayer.config(text=p)
    labelround.config(text="")

#creating buttons
root.bind('<Escape>',lambda e: closeWin(e))
buttonFont= ("Times New Roman", 10,"bold")

buttonRock = Button(root,text="Rock", command= lambda: RPS('Rock'),pady=5,font=buttonFont,justify='center',width=10)
buttonRock.place(x=70,y=200)

buttonpaper = Button(root,text="Paper",  command= lambda: RPS('Paper'),pady=5,font=buttonFont,justify='center',width=10)
buttonpaper.place(x=210,y=200)

buttonScissors = Button(root,text="Scissors",  command= lambda: RPS('Scissors'),pady=5,font=buttonFont,justify='center',width=10)
buttonScissors.place(x=350,y=200)

buttonReset = Button(root,text="Restart",  command= resetgame,pady=5,font=buttonFont,width=10)
buttonReset.place(x=410,y=10)

#calling the  mainloop and game logic for once so that all the buttons are visible 
RPS("")
root.mainloop()