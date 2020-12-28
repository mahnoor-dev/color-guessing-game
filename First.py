import time
import tkinter as tk
from tkinter import ttk, font

# Window
win = tk.Tk()
win.title("Color Game")
win.geometry('10000x10000')
nb = ttk.Notebook(win)
nb.pack(expand=True, fill="both")

#nb.config(bg="#E9FCFC")
#win.resizable(0,0)



COLORS = ["black", "blue", "red", "green", "yellow", "orange", "pink", "brown"]
score = 0
# Tab1 Button
def NEXT():

    #Age_get = age_entrybox.get()
    nb.select(instructions)
    time.sleep(0.5)

def NEXT1():
    nb.select(start_game)
    time.sleep(0.5)

# Tab 1 customization
def tab1():
    global name_entrybox
    global age_entrybox
    global Name_get
    profile = ttk.Frame(nb)
    nb.add(profile, text="PROFILE")




    label_frame0 = tk.LabelFrame(profile, bg='#23B2DC', bd=10)
    label_frame0.place(x=240, y=100)
    inst_label = ttk.Label(label_frame0, font=("system", 18),
                           text="""Meet Jack, Jack is a very fun-loving boy who loves to play games.
                           \nJack is willing to play the color guessing game but the hurdle is
                           \nthat Jack is  color blind. Can you help Jack guessing the color? """)
    inst_label.grid(row=0, column=0)
    label_frame1 = tk.LabelFrame(profile, bg="#23B2DC", bd=5)
    label_frame1.place(x=430, y=350)

    name_label = tk.Label(label_frame1, text="PLAYERS'S NAME: ", bg='#23B2DC', font=("fixedsys", 18))
    name_label.grid(row=0, column=3, padx=4, pady=4)

    age_label = tk.Label(label_frame1, text="PLAYER AGE: ", bg="#23B2DC", font=("fixedsys", 18))
    age_label.grid(row=1, column=3, padx=4, pady=4)


    # entry box
    name_var = tk.StringVar()
    Name_get = name_var.get()
    age_var = tk.StringVar()
    name_entrybox = ttk.Entry(label_frame1, width=35, textvariable=name_var)
    age_entrybox = ttk.Entry(label_frame1, width=35, textvariable=age_var)
    name_entrybox.grid(row=0, column=4, padx=4, pady=4)
    age_entrybox.grid(row=1, column=4, padx=4, pady=4)
    name_entrybox.focus()

    continue_btn = tk.Button(profile, text="SAVE & CONTINUE", bg="#23B2DC", bd=10, font=("fixedsys", 18, "underline"),
                             command=NEXT)
    continue_btn.place(x=540, y=500)

# Tab 2 customization
def tab2():
    global instructions
    instructions = ttk.Frame(nb)
    nb.add(instructions, text="INSTRUCTIONS")

    label_frame2 = tk.LabelFrame(instructions, bg="#23B2DC", bd=10)
    label_frame2.place(x=530, y=70)

    ins_label = tk.Label(label_frame2, text="INSTRUCTIONS: ", bg='#23B2DC', bd=10,
                         font=("system", 24, "bold", "underline"))
    ins_label.grid(row=1, column=5)

    continueto_btn = tk.Button(instructions, text="CONTINUE", bg='#23B2DC', bd=10, font=("system", 18,), command=NEXT1)
    continueto_btn.place(x=550, y=500)
    ins_text = ttk.Label(instructions, text="""1- The time to play the game is 60 seconds
    \n2- Player has to guess the color of the text displayed on the screen
    \n3- Focus on the buttons and choose the name of the color wisely
    \n4- On every right guess 10 points will be increased in player's score
    \n5- The player can also use hints to guess the color""", font=("system", 17))
    ins_text.place(x=260, y=180)

def NEXT3():
    win.destroy()
    import Second

def tab3():
    global start_game

    start_game = ttk.Frame(nb)
    nb.add(start_game, text="START GAME")
    # label_frame3 = ttk.LabelFrame(start_game)
    # label_frame3.pack()
    ready_label = ttk.Label(start_game, text="Are You Ready?", font=("system", 50, "bold"))
    ready_label.place(x=400, y=200)
    start_btn = tk.Button(start_game, text="START GAME", bg='#23B2DC', bd=10, font=("system", 18, "bold", "underline"),
                          command=NEXT3)
    start_btn.place(x=550, y=400)

tab1()
tab2()
tab3()

win.mainloop()