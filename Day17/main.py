from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

Question_bank = []

for question in question_data:
    new_q = Question(question["question"],question["correct_answer"])
    Question_bank.append(new_q)

quiz = QuizBrain(Question_bank)
while quiz.still_has_question():
    quiz.next_question()
    

print("you have completed your quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")
