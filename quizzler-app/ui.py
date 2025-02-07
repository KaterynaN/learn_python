from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20, width=400, height=500)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question = self.canvas.create_text(150,
                                                125,
                                                text="Here will be question",
                                                font=('Arial', 20, "italic"),
                                                fill=THEME_COLOR,
                                                width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        false_image = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_image,
                                highlightthickness=0,
                                bd=0,
                                command=self.send_false)
        self.false_btn.grid(column=0, row=2)

        true_image = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_image,
                               highlightthickness=0,
                               bd=0,
                               command=self.send_true)
        self.true_btn.grid(column=1, row=2)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached end of the game")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def send_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def send_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)