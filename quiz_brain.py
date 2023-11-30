class QuizBrain:
    def __init__(self , question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_no != len(self.question_list)

    def new_question(self):
        choice = input(f"Q{self.question_no + 1}:{self.question_list[self.question_no].question}? (True/False)")
        self.check_answer(choice, self.question_list[self.question_no].answer)
        self.question_no += 1


    def check_answer(self , user_choice , correct_answer):
        if user_choice.lower() == correct_answer.lower():
            print("You got it right!!")
            self.score+=1
        else:
            print("Wrong Answer!!")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_no+1}")
        print("\n")



