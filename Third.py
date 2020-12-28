import time
import tkinter as tk
from tkinter import ttk
from Second import score

Remarks_dict={100:"Oops! Better Luck Next Time",
            150:"Nice Try Can Be Played Much Better",
            200:"Nice Try! You played very Well",
            250:"Woah! Very Well Played"}

# Window3
win3 = tk.Tk()
win3.title("Color Guessing Game")
win3.geometry('10000x10000')
go_label = tk.Label(win3, text="GAME OVER!", font=("Helvetica", 100, "bold"),width=12, height=2,fg="red")
go_label.place(x=170, y=100)

total_score_label = ttk.Label(win3, text="Your Score: ", font=("system", 24, "bold"))
total_score_label.place(x=500, y=400)

final_score_label = ttk.Label(win3, text=f"{score} Points", font=("system", 24, "bold"))
final_score_label.place(x=700, y=400)


def exitF():
    win3.destroy()

exit_btn = tk.Button(win3, text="Exit", bd=10, font=("fixedsys", 18, "underline"),command=exitF)
exit_btn.place(x=610, y=600)


def Remarks():
    if score<=100:
        remarks_label = ttk.Label(win3, text=f"{Remarks_dict.get(100)}", font=("system", 24, "bold"))
        remarks_label.place(x=470, y=500)
    if 100<score<150:
        remarks_label = ttk.Label(win3, text=f"{Remarks_dict.get(150)}", font=("system", 24, "bold"))
        remarks_label.place(x=450, y=500)
    if 150<=score<200:
        remarks_label = ttk.Label(win3, text=f"{Remarks_dict.get(200)}", font=("system", 24, "bold"))
        remarks_label.place(x=475, y=500)
    if score>=250:
        remarks_label = ttk.Label(win3, text=f"{Remarks_dict.get(250)}", font=("system", 24, "bold"))
        remarks_label.place(x=510, y=500)

Remarks()

win3.mainloop()