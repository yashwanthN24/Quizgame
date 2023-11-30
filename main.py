from data import  question_data
from question_model import Question
from quiz_brain import  QuizBrain
question_bank = []
for dic in question_data:
    question_bank.append(Question(dic["question"] , dic["correct_answer"]))

q1 = QuizBrain(question_bank)
while q1.still_has_question():
    q1.new_question()

print("You have completed the quiz!!")
print(f"Your final score is {q1.score}/{q1.question_no}")