from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(150,50)
window.config(padx = 20, pady = 20)

my_lable = Label(text = "is equal to", font = ("Arial",16))
my_lable.grid(column = 0, row = 1)

def cal():
    user_input = input.get()
    x = float(user_input) * 1.609344
    lable_num.config(text = x, font = ("Arial",16) )
    
action = Button(text = "Calculate", command = cal)
action.grid(column = 1, row = 2)
lable_num = Label(text = "", font = ("Arial",16))
lable_num.grid(column = 1, row = 1)

# action2 = Button(text = "CLIKC ME", command = button_click)
# action2.grid(column = 2, row = 0)


input = Entry(width = 10)
input.grid(column = 1, row = 0)
lable_txt = Label(text = "Miles", font = ("Arial",16))
lable_txt.grid(column = 2, row = 0)
lable_txtkm = Label(text = "Km", font = ("Arial",16))
lable_txtkm.grid(column = 2, row = 1)



window.mainloop()

