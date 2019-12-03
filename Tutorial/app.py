import tkinter
import random
from tkinter import *
from tkinter.ttk import *

stats = []


def get_winner(call):
    if random.random() <= (1 / 3):
        throw = "rock"
    elif (1 / 3) < random.random() <= (2 / 3):
        throw = "scissors"
    else:
        throw = "paper"

    if (throw == "rock" and call == "paper") or (throw == "paper" and call == "scissors") \
            or (throw == "scissors" and call == "rock"):
        stats.append('W')
        result = "You won!"
    elif throw == call:
        stats.append('D')
        result = "It's a draw"
    else:
        stats.append('L')
        result = "You lost!"

    global output
    output.config(text="Computer did: " + throw + "\n" + result)


def pass_s():
    get_winner("scissors")


def pass_r():
    get_winner("rock")


def pass_p():
    get_winner("paper")


window = tkinter.Tk()
rock_image = PhotoImage(file=r"C:\Users\Owner\PycharmProjects\Tutorial\rock.png")
paper_image = PhotoImage(file=r"C:\Users\Owner\PycharmProjects\Tutorial\paper.png")
scissors_image = PhotoImage(file=r"C:\Users\Owner\PycharmProjects\Tutorial\scissoes.png")

scissors = tkinter.Button(window, text="Scissors", image=scissors_image, compound=TOP, command=pass_s)
rock = tkinter.Button(window, text="Rock",image=rock_image, compound=TOP, command=pass_r)
paper = tkinter.Button(window, text="Paper",image=paper_image, compound=TOP, command=pass_p)
output = tkinter.Label(window, width=20, fg="red", text="What's your call?")

scissors.pack(side="left")
rock.pack(side="left")
paper.pack(side="left")
output.pack(side="right")
window.mainloop()


