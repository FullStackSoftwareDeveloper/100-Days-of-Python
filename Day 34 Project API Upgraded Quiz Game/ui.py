import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = tkinter.Label(text="Score: 0")
        self.score_label.grid(column=2, row=1)

        self.display_canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.display_canvas.create_text(150, 125, text="Test", width=250)
        self.display_canvas.grid(column=1, row=2, columnspan=2, padx=20, pady=20)

        self.true_button = tkinter.Button(text="True", padx=50, pady=10, command=self.true_pressed)
        self.true_button.grid(column=1, row=3)

        self.false_button = tkinter.Button(text="False", padx=50, pady=10, command=self.false_pressed)
        self.false_button.grid(column=2, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.display_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.display_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.display_canvas.itemconfig(self.question_text, text="You've reached the end")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.display_canvas.config(bg="green")
        else:
            self.display_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)