import tkinter as tk
from tkinter import messagebox


class QuizFrame(tk.Frame):
    def __init__(self, parent, flashcard_manager, quiz_name, switch_frame_callback):
        super().__init__(parent)
        self.flashcard_manager = flashcard_manager
        self.quiz_name = quiz_name
        self.switch_frame_callback = switch_frame_callback
        self.setup_gui()
        self.flashcards = None

        # Ensure that the quiz is selected in FlashcardManager - debug
        quiz_selected = self.flashcard_manager.select_quiz(self.quiz_name)
        if not quiz_selected:
            messagebox.showwarning("Error", "Quiz not found!")
            self.switch_frame_callback('main')
            return

    def setup_gui(self):
        # Display selected quiz name
        selected_label = tk.Label(self, text=f"Selected Quiz: {self.quiz_name}")
        selected_label.pack()

        # Start Quiz button
        start_button = tk.Button(self, text="Start Quiz", command=self.start_quiz)
        start_button.pack()

        # Edit Quiz / Add Flashcards button
        edit_button = tk.Button(self, text="Edit Quiz / Add Flashcards", command=self.edit_quiz)
        edit_button.pack()

        # Back button
        back_button = tk.Button(self, text="Back", command=self.back_to_main)
        back_button.pack()

    def start_quiz(self):
        try:
            self.flashcards = self.flashcard_manager.get_flashcards_for_quiz()
            if self.flashcards:
                self.show_question()
            else:
                messagebox.showinfo("Info", "No flashcards available in this quiz.")
        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    def edit_quiz(self):
        self.switch_frame_callback('edit', self.quiz_name)

    def back_to_main(self):
        self.switch_frame_callback('main')

    def show_question(self):
        # Logic to display questions and handle the quiz
        question_display = tk.Label(self, text=f"First question: {self.flashcards[0][1]}")
        question_display.pack()
