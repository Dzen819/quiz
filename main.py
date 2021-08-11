from question_model import Question
from data import question_data

question_bank = []

for index in range(len(question_data)):
    question = Question(question_data[index]["text"], question_data[index]["answer"])
    question_bank.append(question)


