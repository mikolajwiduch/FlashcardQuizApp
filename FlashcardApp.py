import tkinter as tk
from tkinter import messagebox


class FlashcardApp:
    def __init__(self, root, flashcard_manager):

        self.root = root
        self.flashcard_manager = flashcard_manager
        self.flashcards = []
        self.current_flashcard = None

        # Define widgets inside __init__
        self.quiz_entry = tk.Entry(self.root)
        self.quiz_listbox = tk.Listbox(self.root)
        self.question_entry = tk.Entry(self.root)
        self.answer_entry = tk.Entry(self.root)
        self.question_display = tk.Label(self.root)
        self.user_answer_entry = tk.Entry(self.root)

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

        add_flashcard_button = tk.Button(add_frame, text="Add Flashcard", command=self.add_flashcard)
        add_flashcard_button.grid(row=2, column=0, columnspan=2)

        # Quiz interaction section
        quiz_display_frame = tk.Frame(self.root)
        quiz_display_frame.pack(pady=20)

        start_quiz_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz)
        start_quiz_button.pack(pady=10)

        self.question_display = tk.Label(quiz_display_frame, text="Select a quiz and click 'Start Quiz'", font=('Arial',
                                                                                                                16))
        self.question_display.pack()

        self.user_answer_entry = tk.Entry(quiz_display_frame, width=40)
        self.user_answer_entry.pack(pady=5)

        check_answer_button = tk.Button(quiz_display_frame, text="Check Answer", command=self.check_answer)
        check_answer_button.pack(pady=10)

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

    def select_quiz(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            quiz_name = event.widget.get(index)
            if self.flashcard_manager.select_quiz(quiz_name):
                self.flashcards.clear()
                self.question_display.config(text=f"Selected quiz: {quiz_name}. Click 'Start Quiz' to begin.")
            else:
                messagebox.showwarning("Selection Error", "Quiz not found.")

    def add_flashcard(self):
        question = self.question_entry.get().strip()
        answer = self.answer_entry.get().strip()
        if question and answer:
            try:
                self.flashcard_manager.add_flashcard(question, answer)
                self.question_entry.delete(0, tk.END)
                self.answer_entry.delete(0, tk.END)
                messagebox.showinfo("Success", "Flashcard added.")
            except ValueError as e:
                messagebox.showwarning("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    def start_quiz(self):
        try:
            self.flashcards = self.flashcard_manager.get_flashcards_for_quiz()
            if self.flashcards:
                self.show_question()
            else:
                self.question_display.config(text="No flashcards available in this quiz.")
        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    def show_question(self):
        if self.flashcards:
            self.current_flashcard = self.flashcards.pop(0)
            self.question_display.config(text=self.current_flashcard[1])
            self.user_answer_entry.delete(0, tk.END)
        else:
            self.question_display.config(text="Quiz Completed!")
            self.current_flashcard = None

    def check_answer(self):
        if self.current_flashcard:
            user_answer = self.user_answer_entry.get().strip()
            correct_answer = self.current_flashcard[2]
            if user_answer.lower() == correct_answer.lower():
                self.flashcard_manager.mark_flashcard_answered(self.current_flashcard[0])
                messagebox.showinfo("Correct!", "Correct answer!")
            else:
                messagebox.showerror("Incorrect", f"Wrong answer! The correct answer was: {correct_answer}.")
                self.show_question()
        else:
            messagebox.showwarning("Error", "No question is currently being displayed.")
