class Brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f"Q.{self.question_number}: {current_question.text} [True/False] ")
        if user == current_question.answer:
            return True

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True