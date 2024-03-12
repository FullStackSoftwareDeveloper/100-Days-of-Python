from data import question_data
from question_model import Question
from quiz_brain import Brain

question_bank = []

for i in question_data:
    each_question = Question(i["text"], i["answer"])
    question_bank.append(each_question)

brain = Brain(question_bank)

counter1 = 0
counter2 = 0

while brain.still_has_questions():
    if not brain.still_has_questions():
        break
    else:
        if brain.next_question():
            counter1 += 1
            counter2 += 1
            print(f"Your Answer is correct, score: {counter1}/{counter2}")
        else:
            counter2 += 1
            print(f"Your Answer is wrong, score: {counter1}/{counter2}")