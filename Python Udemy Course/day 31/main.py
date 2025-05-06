from tkinter import *
import pandas 
import random


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")



card_back_img = PhotoImage(file=r"C:\Users\PC\Python Udemy Course\day 31\images\card_back.png")
card_front_img = PhotoImage(file=r"C:\Users\PC\Python Udemy Course\day 31\images\card_front.png")
right_img = PhotoImage(file=r"C:\Users\PC\Python Udemy Course\day 31\images\right.png")
wrong_img = PhotoImage(file=r"C:\Users\PC\Python Udemy Course\day 31\images\wrong.png")
window.config(padx=50,pady=50,bg= BACKGROUND_COLOR)

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(r"C:\Users\PC\Python Udemy Course\day 31\data\french_words.csv")

to_learn = data.to_dict(orient="records")

flip_timer= None
currnt_card = {}

def next_card():
    global currnt_card
    global flip_timer
    if len(to_learn) == 0:
        canvas.itemconfig(card_word, text="All words learned!", fill="black")
        return
    if flip_timer:
        window.after_cancel(flip_timer)

    currnt_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=currnt_card["French"])
    canvas.itemconfig(old_img, image=card_front_img )
    canvas.itemconfig(card_title,fill="black")
    canvas.itemconfig(card_word,fill="black"  )
    
    flip_timer = window.after(3000, card_back)
def card_back():
    global currnt_card

    window.after_cancel(flip_timer)
    canvas.itemconfig(old_img, image=card_back_img )
    canvas.itemconfig(card_title,text="English",fill="white" )
    canvas.itemconfig(card_word,text=currnt_card["English"],fill="white")
def isknown():
    global to_learn
    to_learn.remove(currnt_card)
    pandas.DataFrame(to_learn).to_csv("words_to_learn.csv", index=False)
    next_card()

canvas = Canvas(width=800,height=526)
old_img = canvas.create_image(400 , 263,image = card_front_img)
card_title = canvas.create_text(400,150, text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263, text="",font=("Ariel",40,"bold"))

canvas.config(bg= BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2 )

unknown_button = Button(image=wrong_img,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)
check_img = Button(image = right_img,highlightthickness=0,command=isknown)
check_img.grid(row = 1,column=1)

next_card()


window.mainloop()


