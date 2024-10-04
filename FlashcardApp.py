import tkinter as tk
from tkinter import messagebox


class FlashcardApp:
    def __init__(self, root, flashcard_manager):
        self.root = root
        self.flashcard_manager = flashcard_manager
        self.flashcards = []
        self.current_flashcard = None

        # Set up the GUI
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Flashcard Quiz App")

        # Quiz creation selection
        quiz_frame = tk.Frame(self.root)
        quiz_frame.pack(pady=10)

        quiz_label = tk.Label(quiz_frame, text="Create New Quiz:")
        quiz_label.pack(side=tk.LEFT)

        self.quiz_entry = tk.Entry(quiz_frame)
        self.quiz_entry.pack(side=tk.LEFT)

        create_quiz_button = tk.Button(quiz_frame, text="Create Quiz", command=self.create_quiz)
        create_quiz_button.pack(side=tk.LEFT)

        # Quiz selection section
        select_frame = tk.Frame(self.root)
        select_frame.pack(pady=10)

        select_label = tk.Label(select_frame, text="Available Quizzes:")
        select_label.pack()

        self.quiz_listbox = tk.Listbox(select_frame)
        self.quiz_listbox.pack()
        self.quiz_listbox.bind('<<ListboxSelect>>', self.select_quiz)

        self.load_quizzes()

        # Flashcard addition section
        add_frame = tk.Frame(self.root)
        add_frame.pack(pady=10)

        question_label = tk.Label(add_frame, text="Question:")
        question_label.grid(row=0, column=0)

        self.question_entry = tk.Entry(add_frame, width=50)
        self.question_entry.grid(row=0, column=1)

        answer_label = tk.Label(add_frame, text="Answer:")
        answer_label.grid(row=1, column=0)

        self.answer_entry = tk.Entry(add_frame, width=50)
        self.answer_entry.grid(row=1, column=1)

