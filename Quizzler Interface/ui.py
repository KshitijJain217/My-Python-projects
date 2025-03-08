from tkinter import *
from quiz_brain import QuizBrain
# slate blue = #3a445d #2e3a59 #9bc4e2
#  default color = #375362

THEME_COLOR1 = "#9bc4e2"
THEME_COLOR2 = "#2e3a59"
FONT1 = ("Arial", 18, "italic")
FONT2 = ("Arial", 16, "bold")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("The QuizBrain")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR1)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR1, font=FONT2)
        self.score_label.grid(row=0, column=1)

        # create an out of questions label to display when the quiz is over

        self.canvas = Canvas(width=340, height=250, bg="white")
        # here the 'width' allows the question text to fit inside border
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="The Question", fill=THEME_COLOR2, font=FONT1)
        self.canvas.grid(row=1, column=0, columnspan=3, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.\n"
                                                            f"Your final score is: {self.quiz.score}/10")
            # here is a bug that makes score display 1 less than the actual score
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
