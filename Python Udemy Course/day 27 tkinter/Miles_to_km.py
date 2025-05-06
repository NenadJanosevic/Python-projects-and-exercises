from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(150,50)
window.config(padx = 20, pady = 20)

my_lable = Label(text ="I'am a Label", font = ("Arial",24))
my_lable.config(text = "New text")
my_lable.grid(column = 0, row = 0)

def button_click():
    my_lable.config(text = input.get())
     
    
action = Button(text = "CLIKC ME", command = button_click)
action.grid(column = 1, row = 1)

action2 = Button(text = "CLIKC ME", command = button_click)
action2.grid(column = 2, row = 0)