import tkinter as tk
from tkinter import messagebox


class QuizFrame(tk.Frame):
    def __init__(self, parent, flashcard_manager, quiz_name, switch_frame_callback):
        super().__init__(parent)
        self.flashcard_manager = flashcard_manager
        self.quiz_name = quiz_name
        self.switch_frame_callback = switch_frame_callback
        self.setup_gui()

    def setup_gui(self):
        selected_label = tk.Label(self, text=f"Selected Quiz: {self.quiz_name}")
        selected_label.pack()

        start_button = tk.Button(self, text="Start Quiz", command=self.start_quiz)
        start_button.pack()

        edit_button = tk.Button(self, text="Edit Quiz / Add Flashcard", command=self.edit_quiz)

    def start_quiz(self):
        try:
            self.flashcards = self.flashcard_manager.get_flashcards_for_quiz()
            if self.flashcards:
                self.show_question()
            else:
                self.question_display.config(text="No flashcards available in this quiz.")
        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    def edit_quiz(self):
        self.switch_frame_callback('edit', self.quiz_name)
