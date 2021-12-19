"""

Quiz aaplication in flashcard style

@author: Ishan Shah
"""

from tkinter import *
import pandas
import random
reps = 0
timer_window=None
BACKGROUND_COLOR = "#B1DDC6"
data={}
ques=ans=number=""
language=score=""


"""
Initialise the data
"""
def start():
    global data
    start["state"]=DISABLED
    reset["state"]=NORMAL
    csv_read=pandas.read_csv("data/french_words.csv")
    data=csv_read.to_dict()
    counter(3)

"""
 Reset the data
"""
def reset():
    right["state"] = DISABLED
    wrong["state"] = DISABLED
    start["state"]= NORMAL
    reset["state"]= DISABLED
    clock_canvas.itemconfig(score, text="Score: 0")
    window.after_cancel(timer_window)

"""
 if wrong answer, words stays in the data
"""
def wrong_ans():
    right["state"] = DISABLED
    wrong["state"] = DISABLED
    counter(3)

"""
 if correct answer, points are incrmented and word deleted from data
"""
def right_ans():
    del data["French"][number]
    del data["English"][number]
    right["state"] = DISABLED
    wrong["state"] = DISABLED
    points=101-len(data["French"])
    clock_canvas.itemconfig(score,text="Score: "+str(points))
    counter(3)

"""
 counter for the clock
"""
def counter(count):
    global ques, ans, number
    if count==3:
        question_canvas.itemconfig(q_image, image=question_photo)
        total=len(data["French"])
        number=random.randint(0,total)
        ques=data["French"][number]
        ans=data["English"][number]
        question_canvas.itemconfig(language, text="French")
        question_canvas.itemconfig(question, text=ques)
    if count>0:
        clock_canvas.itemconfig(timer,text=str(count))
        timer_window=window.after(1000,counter,count-1)
    else:
        question_canvas.itemconfig(language, text="English")
        question_canvas.itemconfig(question, text=ans)
        right["state"]=NORMAL
        wrong["state"] = NORMAL
        clock_canvas.itemconfig(timer,text="Enter choice")
        question_canvas.itemconfig(q_image, image=ans_photo)

# ----------------------------------------main-----------------------------------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)


question_canvas = Canvas(width=800,height=526,highlightthickness=0)
question_photo=PhotoImage(file="images/card_front.png")
ans_photo=PhotoImage(file="images/card_back.png")
q_image=question_canvas.create_image(400,260,image=question_photo)
language=question_canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
question=question_canvas.create_text(400,263,text="Welcome",font=("Arial",60))
question_canvas.grid(row=0,columnspan=True)


clock_canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR
                      )
clock_photo=PhotoImage(file="images/clock.png")
clock_canvas.create_image(110,263,image=clock_photo)
timer=clock_canvas.create_text(110,263,text="Timer",font=("Arial",20,"bold"))
score=clock_canvas.create_text(400,100,text="Score: 0",font=("Arial",20,"bold"))
clock_canvas.grid(row=0,column=2)

right_photo=PhotoImage(file="images/right.png")
right=Button(image=right_photo,command=right_ans)
right.grid(row=1,column=1)
right["state"] = DISABLED

wrong_photo=PhotoImage(file="images/wrong.png")
wrong=Button(image=wrong_photo,command=wrong_ans)
wrong.grid(row=1,column=0)
wrong["state"] = DISABLED


start=Button(text="Start", command=start)
start.place(x=1000,y=565)

reset=Button(text="Reset", command=reset,state=DISABLED)
reset.place(x=1100,y=565)

window.mainloop()



