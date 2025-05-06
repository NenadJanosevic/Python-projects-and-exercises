from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_text = item["text"]
    question_anwser= item["answer"]
    new_question = Question(q_text=question_text,q_answer= question_anwser)
    question_bank.append(new_question)

quiz = QuizBrain(q_list = question_bank)
while quiz.loop():
    quiz.next_question()

print("You have complited the quiz")
print(f"Your finale score was: {quiz.score}/{quiz.question_number}")
    