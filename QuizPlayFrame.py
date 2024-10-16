import tkinter as tk
from tkinter import messagebox
import random


class QuizPlayFrame(tk.Frame):
    def __init__(self, parent, flashcard_manager, quiz_name, switch_frame_callback):
        super().__init__(parent)
        self.flashcard_manager = flashcard_manager
        self.quiz_name = quiz_name
        self.switch_frame_callback = switch_frame_callback
        self.current_question = None
        self.flashcards = []
        self.setup_gui()

        # Load flashcards and select quiz
        quiz_selected = self.flashcard_manager.select_quiz(self.quiz_name)
        if quiz_selected:
            self.flashcards = self.flashcard_manager.get_flashcards_for_quiz()
            self.show_next_question()
        else:
            messagebox.showwarning("Error", "Quiz not found!")
            self.switch_frame_callback('main')

    def setup_gui(self):
        # Question label
        self.question_label = tk.Label(self, text="Question:")
        self.question_label.grid(row=0, column=0, padx=10, pady=10)

        # Answer entry
        self.answer_entry = tk.Entry(self)
        self.answer_entry.grid(row=1, column=0, padx=10, pady=10)

        # Check answer button
        self.check_button = tk.Button(self, text="Check Answer", command=self.check_answer)
        self.check_button.grid(row=2, column=0, padx=10, pady=10)

        # Submit button
        self.submit_button = tk.Button(self, text="Submit Answer", command=self.submit_answer)
        self.submit_button.grid(row=3, column=0, padx=10, pady=10)

        # Next question button
        self.next_button = tk.Button(self, text="Next Question", command=self.show_next_question)
        self.next_button.grid(row=4, column=0, padx=10, pady=10)

        # Back button
        self.back_button = tk.Button(self, text="Back", command=self.back_to_quiz)
        self.back_button.grid(row=5, column=0, padx=10, pady=10)

    def show_next_question(self):
        if self.flashcards:
            self.current_question = random.choice(self.flashcards)
            self.question_label.config(text=f"Question: {self.current_question[1]}")
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Quiz Completed!", "No more unanswered questions!")
            self.switch_frame_callback('main')

    def check_answer(self):
        if self.current_question:
            answer = self.current_question[2]
            messagebox.showinfo("Answer", f"The correct answer is: {answer}")

    def submit_answer(self):
        if self.current_question:
            user_answer = self.answer_entry.get().strip()
            if user_answer.lower() == self.current_question[2].lower():
                messagebox.showinfo("Correct!", "You answered correctly")
                self.flashcard_manager.mark_flashcard_answered(self.current_question[0])
                self.flashcards.remove(self.current_question)
            else:
                messagebox.showinfo("Incorrect", "That's not correct answer. Try Again.")

    def back_to_quiz(self):
        self.switch_frame_callback('quiz', self.quiz_name)
