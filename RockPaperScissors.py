from math import exp
import random
from tkinter import *

root=Tk()
root.title("Rock, Paper or Scrissors")
root.geometry('500x280')
root.resizable(0,0)


textFont=("Times New Roman", 40, "bold")
ScoreFont=("Times New Roman", 15, "bold")
background="black"
foreground="white"
root['background']='black'
labelcpu= Label(root,font=textFont,bg=background,fg=foreground)
# labelcpu.grid(row=0,column=0,padx=30,pady=30)
labelcpu.place(x=50,y=50)
labelplayer= Label(root,font=textFont,bg=background,fg=foreground)
# labelplayer.grid(row=0,column=2,padx=30,pady=30)
labelplayer.place(x=250,y=50)
labelround= Label(root,font=ScoreFont,bg=background,fg=foreground)
# labelround.grid(row=1,padx=30,pady=30,column=1)
labelround.place(x=230,y=150,anchor="center")


cpuScore = [0]
playerScore = [0]
choices = ["Rock", "Paper", "Scissors"]


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

def closeWin(e):
    root.destroy()

def resetgame():
    cpuScore[0]=0
    playerScore[0]=0
    cpu=f"CPU:{cpuScore[0]}"
    labelcpu.config(text=cpu)
    p=f"Player:{playerScore[0]}"
    labelplayer.config(text=p)
    labelround.config(text="")

root.bind('<Escape>',lambda e: closeWin(e))
buttonFont= ("Times New Roman", 10,"bold")
buttonRock = Button(root,text="Rock", command= lambda: RPS('Rock'),pady=5,font=buttonFont,justify='center',width=10)
# buttonRock.grid(row=2,column=0,pady=30)
buttonRock.place(x=70,y=200)
buttonpaper = Button(root,text="Paper",  command= lambda: RPS('Paper'),pady=5,font=buttonFont,justify='center',width=10)
# buttonpaper.grid(row=2,column=1)
buttonpaper.place(x=210,y=200)
buttonScissors = Button(root,text="Scissors",  command= lambda: RPS('Scissors'),pady=5,font=buttonFont,justify='center',width=10)
# buttonScissors.grid(row=2,column=2)
buttonScissors.place(x=350,y=200)
buttonReset = Button(root,text="Restart",  command= resetgame,pady=5,font=buttonFont,width=10)
buttonReset.place(x=410,y=10)
RPS("")
root.mainloop()