import tkinter as tk
from tkinter import messagebox


class MainFrame(tk.Frame):
    def __init__(self, parent, flashcard_manager, switch_frame_callback):
        super().__init__(parent)
        self.flashcard_manager = flashcard_manager
        self.switch_frame_callback = switch_frame_callback

        # Define widgets inside __init__
        self.quiz_entry = None
        self.quiz_listbox = None
        self.go_to_quiz_buttons = None

        # Set up the GUI
        self.setup_gui()

    def setup_gui(self):
        # Quiz creation section
        create_quiz_label = tk.Label(self, text="Create New Quiz:")
        create_quiz_label.grid(row=0, column=0)

        self.quiz_entry = tk.Entry(self)
        self.quiz_entry.grid(row=0, column=1)

        create_button = tk.Button(self, text="Create Quiz", command=self.create_quiz)
        create_button.grid(row=0, column=2)

        # Available quizzes section
        quizzes_label = tk.Label(self, text="Available Quizzes:")
        quizzes_label.grid(row=1, column=0, columnspan=3)

        self.quiz_listbox = tk.Listbox(self)
        self.quiz_listbox.grid(row=2, column=0, columnspan=2)

        self.load_quizzes()

    def create_quiz(self):
        quiz_name = self.quiz_entry.get().strip()
        if quiz_name:
            self.flashcard_manager.create_quiz(quiz_name)
            self.quiz_entry.delete(0, tk.END)
            self.load_quizzes()
        else:
            messagebox.showwarning("Input Error", "Please enter a quiz name.")

    def load_quizzes(self):
        quizzes = self.flashcard_manager.db_manager.get_quizzes()
        self.quiz_listbox.delete(0, tk.END)
        for quiz in quizzes:
            self.quiz_listbox.insert(tk.END, quiz[1])

        # Go to quiz button
        self.update_quiz_buttons()

    def update_quiz_buttons(self):
        if self.go_to_quiz_buttons:
            for button in self.go_to_quiz_buttons:
                button.destroy()  # Destroy previous buttons

        self.go_to_quiz_buttons = []
        for i in range(self.quiz_listbox.size()):
            go_to_quiz_button = tk.Button(self, text="Go to Quiz",
                                          command=lambda idx=i: self.go_to_quiz(idx))
            go_to_quiz_button.grid(row=2 + i, column=2)
            self.go_to_quiz_buttons.append(go_to_quiz_button)

    def go_to_quiz(self, index):
        selected_quiz = self.quiz_listbox.get(index)
        self.switch_frame_callback('quiz', selected_quiz)
