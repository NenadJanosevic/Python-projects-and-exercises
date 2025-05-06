from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")

canvas = Canvas(width = 300, height = 224, highlightthickness = 0)

card_back_img = PhotoImage(file=r"C:\Users\PC\Python Udemy Course\day 31 \images\card_back.png")
card_front_img = PhotoImage(file=r"C:\Users\PC\Python Udemy Course\day 31 \images\card_front.png")
right_img = PhotoImage(file=r"C:\Users\PC\Python Udemy Course\day 31 \images\right.png")
wrong_img = PhotoImage(file=r"C:\Users\PC\Python Udemy Course\day 31 \images\wrong.png")


window.mainloop()


