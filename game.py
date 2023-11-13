from tkinter import *
from PIL import Image, ImageTk
from random import randint

# front page
page = Tk()
page.title("Rock Paper Scissors")
page.configure(background="purple")

# picture
rockuser = ImageTk.PhotoImage(Image.open("rockuser.png"))
paperuser = ImageTk.PhotoImage(Image.open("paperuser.png"))
scissorsuser = ImageTk.PhotoImage(Image.open("scissorsuser.png"))
rockcomp = ImageTk.PhotoImage(Image.open("rockcomp.png"))
papercomp = ImageTk.PhotoImage(Image.open("papercomp.png"))
scissorscomp = ImageTk.PhotoImage(Image.open("scissorscomp.png"))

# insert picture
user_label = Label(page, image=scissorsuser, bg = "purple")
comp_label = Label(page, image=scissorscomp, bg = "purple")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#scores
userscore = Label(page, text=0, font=100, bg="purple", fg="white")
compscore = Label(page,text=0, font=100, bg="purple",fg="white" )
compscore.grid(row=1, column=1)
userscore.grid(row=1, column=3)

# indicators for sides (computer or user)
user_indicator = Label(font=50, text="User", bg="purple", fg="white")
comp_indicator = Label(font=50, text="Computer", bg="purple", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# text box for displaying wins or losses
msg = Label(font=50, bg="white", fg="white")
msg.grid(row=3, column=2)

# to update texts
def updateMessage():
    x = int(msg["text"])
    msg["text"] = str(x)
def updateMessage(self):
    pass

# to update user's score
def updateUserScore():
    newscore = int(userscore["text"])
    newscore += 1
    userscore["text"] = str(newscore)

# to update computer's score
def updateCompScore():
    newscore = int(compscore["text"])
    newscore += 1
    compscore["text"] = str(newscore)

# to check who is the winner
def checkWinner(user, comp):
    if user == comp:
        updateMessage("It is a tie.")
        updateCompScore()

    elif user == "rock":
        if comp == "paper":
            updateMessage("Well Fuck :/ You Lost. Try Again.")
            updateCompScore()
        else:
            updateMessage("Congratulations! You finally won, you little shit!")
            updateUserScore()
    
    elif user == "paper":
        if comp == "rock":
            updateMessage("Congratulations! You finally won, you little shit!")
            updateUserScore()
        else:
            updateMessage("Well Fuck :/ You Lost. Try Again.")
            updateCompScore()
    
    elif user == "scissors":
        if comp == "rock":
            updateMessage("Well Fuck :/ You Lost. Try Again.")
            updateCompScore()
        else:
            updateMessage("Congratulations! You finally won, you little shit!")
            updateUserScore()
    
    else:
        pass

# generating random choices from computer
choices = ["rock", "paper", "scissors"]

def pictureAccToChoice(x):
# to get image according to computer's choice
    compChoice = choices[randint(0,2)]
    if compChoice=="rock":
        comp_label.configure(image=rockcomp)
    elif compChoice=="paper":
        comp_label.configure(image=papercomp)
    else:
        comp_label.configure(image=scissorscomp)

# to get image according to user's choice
    if x=="rock":
        user_label.configure(image=rockuser)
    elif x=="paper":
        user_label.configure(image=paperuser)
    else:
        user_label.configure(image=scissorsuser)
    
    checkWinner(x, compChoice)
#buttons
rock = Button(page, width=20, height=2, text="Rock", command=lambda:pictureAccToChoice("rock"), bg="blue", fg="white").grid(row=2, column=1)
paper = Button(page, width=20, height=2, text="Paper", command=lambda:pictureAccToChoice("paper"), bg="blue", fg="white").grid(row=2, column=2)
scissors = Button(page, width=20, height=2, text="Scissors", command=lambda:pictureAccToChoice("scissors"), bg="blue", fg="white").grid(row=2, column=3)


page.mainloop()
