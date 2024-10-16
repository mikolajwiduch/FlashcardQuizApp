import tkinter as tk
from tkinter import messagebox
import random


class QuizPlayFrame(tk.Frame):
    def __init__(self, parent, flashcard_manager, quiz_name, switch_frame_callback):
        super().__init__(parent)
        self.flashcard_manager = flashcard_manager
        self.quiz_name = quiz_name
        self.switch_frame_callback = switch_frame_callback
        self.question_label = None
        self.answer_entry = None
        self.current_question_index = 0
        self.flashcards = self.flashcard_manager.get_flashcards_for_quiz()

        if self.flashcards:
            self.setup_gui()

    def setup_gui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Question label
        self.question_label = tk.Label(self, text="", font=("Helvetica", 16), wraplength=400)
        self.question_label.grid(row=0, column=1, pady=20)

        # Answer entry
        answer_label = tk.Label(self, text="Your Answer:", font=("Helvetica", 12))
        answer_label.grid(row=1, column=1)

        self.answer_entry = tk.Entry(self, font=("Helvetica", 12))
        self.answer_entry.grid(row=2, column=1, pady=10)

        # Check Answer
        check_button = tk.Button(self, text="Check Answer", command=self.check_answer)
        check_button.grid(row=2, column=2, padx=10)

        # Submit button
        submit_button = tk.Button(self, text="Submit", command=self.submit_answer)
        submit_button.grid(row=3, column=1, pady=10)

        # Previous and Next buttons
        prev_button = tk.Button(self, text="Previous Question", command=self.prev_question)
        prev_button.grid(row=4, column=0, pady=20)

        next_button = tk.Button(self, text="Next Question", command=self.next_question)
        next_button.grid(row=4, column=2, pady=20)

        # Back button
        back_button = tk.Button(self, text="Back", command=self.back_to_quiz)
        back_button.grid(row=5, column=0, padx=10, pady=20)

        self.show_question(self.current_question_index)

    def show_question(self, index):
        self.answer_entry.delete(0, tk.END)
        self.question_label.config(text=self.flashcards[index][1])

    def check_answer(self):
        correct_answer = self.flashcards[self.current_question_index][2]
        answer = self.answer_entry.get().strip()
        if answer == correct_answer:
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", "Your answer is incorrect. Try again!")

    def submit_answer(self):
        self.flashcard_manager.mark_flashcard_answered(self.flashcards[self.current_question_index][0])
        self.flashcards = self.flashcard_manager.get_flashcards_for_quiz()  # Refresh questions

    def prev_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_question(self.current_question_index)

    def next_question(self):
        if self.current_question_index < len(self.flashcards) - 1:
            self.current_question_index += 1
            self.show_question(self.current_question_index)

    def back_to_quiz(self):
        self.switch_frame_callback('quiz', self.quiz_name)
