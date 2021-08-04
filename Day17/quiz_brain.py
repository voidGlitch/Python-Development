class QuizBrain :
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_question(self):
        number_of_question = len(self.question_list)
        if self.question_number < number_of_question :
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number} : {current_question.text}(true / false) :")
        self.check_answer(user_answer,current_question.answer)
    
    

    def check_answer(self,user_answer , correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you are correct")
            self.score += 1
            
        else :
            print("you are wrong")
        print(f"the correct answer is {correct_answer}")
        print(f"your score is {self.score}/{self.question_number}")
        print("\n")