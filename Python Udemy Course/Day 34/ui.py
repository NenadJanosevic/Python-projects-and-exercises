from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR)
        
        self.lable = Label(text="score:0",fg="white",bg = THEME_COLOR,font=("Arial", 20, "italic"))
        self.lable.grid(column=1,row= 0)
        
        self.canvas = Canvas(width=300,height=250,)
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text="sss",fill="black", font=("Arial",20,"italic"))
        self.canvas.grid(column=0 ,row=1,columnspan=2,pady=20)

        self.imgy = PhotoImage(file=r"C:\Users\PC\Python Udemy Course\Day 34\images\true.png")
        self.button_1 = Button(image=self.imgy,command=self.right_anwser) 
        self.button_1.grid(column=0 ,row=2,pady=20)

        self.imgx = PhotoImage(file=r"C:\Users\PC\Python Udemy Course\Day 34\images\false.png")
        self.button_2 = Button(image=self.imgx,command=self.wrong_anwser)
        self.button_2.grid(column=1 ,row=2,pady=20)
        
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.lable.config(text=f"Score = {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,text = q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="End\nCreduts:\nNenad Janosevic")
            self.button_1.config(state="disabled")
            self.button_2.config(state="disabled")
            
    def right_anwser(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
  
    def wrong_anwser(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)  #change: function reference without parentheses
