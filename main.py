from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for index in range(len(question_data)):
    question = Question(question_data[index]["question"], question_data[index]["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!\nYour final score was: {quiz.score}/{len(question_bank)}")
