from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
timer = None
mark = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reser_timer():
    global reps
    global mark
    window.after_cancel(timer)
    reps = 0
    mark = ""
    text_check.config(text=mark)
    text_timer.config(text="Timer")
    canvas.itemconfig(timer_text,text = "00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    shot_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        text_timer.config(text="Long break",font=(FONT_NAME,35,"bold"),fg = RED,bg = YELLOW )
    elif reps % 2 == 0:
        count_down(shot_break_sec)
        text_timer.config(text="Short breka",font=(FONT_NAME,35,"bold"),fg = PINK,bg = YELLOW )
    else:
        count_down(work_sec)
        text_timer.config(text="Work Bitch",font=(FONT_NAME,35,"bold"),fg = GREEN,bg = YELLOW )
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = (count % 60 )
    if count_sec == 0:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        global mark
        start_timer()
        
        for _ in range (math.floor(reps / 2)):
            mark += "✔"
            text_check.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx =100, pady = 150, bg = YELLOW)

fg = GREEN
canvas = Canvas(width = 300, height = 224, bg=YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(150,112, image = tomato_img )
timer_text = canvas.create_text(150,130, text = "00:00", fill = "white", font = (FONT_NAME,35,"bold"))
canvas.grid(column=1 ,row=1)

text_timer = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg = GREEN,bg = YELLOW )
text_timer.grid(column=1 ,row=0)
text_check = Label(font=(FONT_NAME,30,"bold"),fg = GREEN,bg = YELLOW )
text_check.grid(column=1 ,row=3)
button_Start = Button(text="Start", highlightthickness = 0,command=start_timer)
button_Start.grid(column=0 ,row=2)
button_Reset = Button(text="Reset", highlightthickness = 0, command=reser_timer)
button_Reset.grid(column=2 ,row=2)









#Postavljanej prozor programa na sredini ekrana
window_width = 600  
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
#----------------------------------------------------------- #


window.mainloop()