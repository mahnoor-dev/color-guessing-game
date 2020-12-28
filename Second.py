import random
import tkinter as tk
from tkinter import messagebox

new_win=tk.Tk()
new_win.title("Color Guessing Game")
new_win.geometry("10000x10000")
#new_win.resizable(0,0)

COLORS=["black","blue","red","green","yellow","orange","pink","brown"]
BTN_COLORS=["black","blue","red","green","#FFCD00","#FF9300","#FF5EB8","#92611E"]


Hint_Dict={"black":"Baa Baa Black sheep, have you any wool?",
           "blue":"Roses are red, vloilets are ???",
           "green":"Which color comes into your min when you hear the word FRESH VEGETABLES",
           "pink":"Try remembering the famous PANTHER cartoon?",
           "yellow":"Remember Tom n Jerry? Jerry likes cheese",
           "brown":"Chocolate is a good mood food, Think now!",
           "red":"Imagine a farm of fresh Strawberries.. yummy!",
           "orange":"May be this color is also the name of a fruit"}
score=0
timeleft=60
C = tk.Canvas(new_win, height=700, width=1500)
img = tk.PhotoImage(file='E:\\Python-Color-Game-master\\abc.png')

C.create_image(500, 500, image=img)
C.place(x=0, y=0)

identify_label = tk.Label(C, text="***Identify The Color Below***" ,font=("system", 10), fg="red")
identify_label.place(x=580, y=175)

identifybtn_label = tk.Label(C, text="***Select The Name Of The Color from Below ***" ,font=("system", 10), fg="red")
identifybtn_label.place(x=510, y=495)

def BUTTON():
    btn_label_frame=tk.LabelFrame(new_win)
    btn_label_frame.place(x=310,y=520)


    def BLACK():

        black_btn=tk.Button(btn_label_frame,text="BLACK",fg="white",bg=str(BTN_COLORS[1]),width=20,height=3,font=("system",14,"bold"),command=COMMAND_BLACK)
        black_btn.grid(row=4,column=1,padx=5,pady=3)

    BLACK()

    def BLUE():
        blue_btn=tk.Button(btn_label_frame,text="BLUE",fg="white",bg=str(BTN_COLORS[2]),width=20,height=3,font=("system",14,"bold"),command=COMMAND_BLUE)
        blue_btn.grid(row=4,column=2,padx=5,pady=3)

    BLUE()

    def GREEN():
        green_btn=tk.Button(btn_label_frame,text="GREEN",fg="white",bg=str(BTN_COLORS[4]),width=20,height=3,font=("system",14,"bold"),command=COMMAND_GREEN)
        green_btn.grid(row=4,column=3,padx=5,pady=3)

    GREEN()

    def PINK():
        pink_btn=tk.Button(btn_label_frame,text="PINK",fg="white",bg=str(BTN_COLORS[3]),width=20,height=3,font=("system",14,"bold"),command=COMMAND_PINK)
        pink_btn.grid(row=4,column=4,padx=5,pady=3)

    PINK()

    def YELLOW():
        yellow_btn=tk.Button(btn_label_frame,text="YELLOW",fg="white",bg=str(BTN_COLORS[5]),width=20,height=3,font=("system",14,"bold"),command=COMMAND_YELLOW)
        yellow_btn.grid(row=5,column=1,padx=5,pady=3)

    YELLOW()

    def ORANGE():
        orange_btn=tk.Button(btn_label_frame,text="ORANGE",fg="white",bg=str(BTN_COLORS[6]),width=20,height=3,font=("system",14,"bold"),command=COMMAND_ORANGE)
        orange_btn.grid(row=5,column=2,padx=5,pady=3)

    ORANGE()

    def RED():
        red_btn=tk.Button(btn_label_frame,text="RED",fg="white",bg=str(BTN_COLORS[7]),width=20,height=3,font=("system",14,"bold"),command=COMMAND_RED)
        red_btn.grid(row=5,column=3,padx=5,pady=3)

    RED()

    def BROWN():
        brown_btn=tk.Button(btn_label_frame,text="BROWN",fg="white",bg=str(BTN_COLORS[0]),width=20,height=3,font=("system",14,"bold"),command=COMMAND_BROWN)
        brown_btn.grid(row=5,column=4,padx=5,pady=3)

    BROWN()

def COMMAND_BLACK():

    global Answer
    global score
    Answer="black"
    nextColour()
    change_color()

    global score
    Answer="blue"
def COMMAND_BLUE():
    global Answer
    nextColour()
    change_color()

def COMMAND_GREEN():
    global Answer
    global score
    Answer="green"
    nextColour()
    change_color()
def COMMAND_PINK():
    global Answer
    global score
    Answer="pink"
    nextColour()
    change_color()

def COMMAND_YELLOW():
    global Answer
    global score
    Answer="yellow"
    nextColour()
    change_color()
def COMMAND_ORANGE():
    global Answer
    global score
    Answer="orange"
    nextColour()
    change_color()
def COMMAND_RED():
    global Answer
    global score
    Answer="red"
    nextColour()
    change_color()
def COMMAND_BROWN():
    global Answer
    global score
    Answer="brown"
    nextColour()
    change_color()

def change_color():
    global  label
    random.shuffle(COLORS)
    x= COLORS[0]
    y=COLORS[1]
    label =tk.Label(new_win,text=str(x),height=2,font=('fixedsys',75,'bold'),fg=str(y),border=1,width=10,bg="white",borderwidth=2, relief="solid")
    label.place(x=470,y=200)


def countdown():
    global timeleft
    # if a game is in play
    if timeleft > 0:
        # decrement the timer.
        timeleft -= 1
        timeLabel.config(text="TIME LEFT: "+ str(timeleft))

        timeLabel.after(1000, countdown)
    else:
        timeUP()

def nextColour():
    global score
    global timeleft
    # if a game is currently in play
    if timeleft > 0:

        if Answer== COLORS[1]:
            score += 10

        random.shuffle(COLORS)
        label.config(fg=str(COLORS[1]), text=str(COLORS[0]))

        # update the score.
        scoreLabel.config(text="SCORE: " + str(score))


def time():
    global timeLabel
    global scoreLabel
    timeLabel = tk.Label(new_win, text="TIME LEFT: " + str(timeleft), font=('system', 18,"bold",))
    timeLabel.place(x=1000,y=100)
    scoreLabel = tk.Label(new_win, text="SCORE:00",font=('system', 18,"bold",))
    scoreLabel.place(x=1000,y=150)

def Hint_Command():
    if COLORS[1]=="black":
        messagebox.showinfo("HINT",str(Hint_Dict.get("black")))
    if COLORS[1]=="blue":
        messagebox.showinfo("HINT", str(Hint_Dict.get("blue")))
    if COLORS[1]=="green":
        messagebox.showinfo("HINT", str(Hint_Dict.get("green")))
    if COLORS[1]=="pink":
        messagebox.showinfo("HINT", str(Hint_Dict.get("pink")))
    if COLORS[1]=="yellow":
        messagebox.showinfo("HINT", str(Hint_Dict.get("yellow")))
    if COLORS[1]=="brown":
        messagebox.showinfo("HINT", str(Hint_Dict.get("brown")))
    if COLORS[1]=="red":
        messagebox.showinfo("HINT", str(Hint_Dict.get("red")))
    if COLORS[1]=="orange":
        messagebox.showinfo("HINT", str(Hint_Dict.get("orange")))

def Hint():
    Hint_button=tk.Button(new_win,text="HINT",fg="black", bg="#23B2DC",width=10,bd=5,height=2,font=("system",20,"bold"),command=Hint_Command)
    Hint_button.place(x=100,y=100)

def timeUP():
    if timeleft==0:
        new_win.destroy()
        import Third

Hint()
BUTTON()
change_color()
time()
countdown()

new_win.mainloop()
