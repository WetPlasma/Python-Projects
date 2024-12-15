from question_model import Question
from data import question_data
from quiz_brain import quiz_brain
question_bank =[]


for item in question_data:
    
    new_question=Question(item["text"],item["answer"])
    question_bank.append(new_question)

quiz=quiz_brain(question_bank)
while True:
    if not quiz.next_question():
        if not quiz.stillhasq():
            break
        break
    else:
        continue