import tkinter as tk
from tkinter import messagebox


class FlashcardManagementFrame(tk.Frame):
    def __init__(self, parent, flashcard_manager, quiz_name, switch_frame_callback):
        self.parent = parent
        super().__init__(parent)
        self.flashcard_manager = flashcard_manager
        self.quiz_name = quiz_name
        self.setup_gui()
        self.switch_frame_callback = switch_frame_callback

    def setup_gui(self):
        label = tk.Label(self, text=f"Editing {self.quiz_name}")
        label.pack()

        # Widgets for editing/deleting flashcards & editing quizzes

        # Add flashcard section
        add_question_label = tk.Label(self, text="New Question:")
        add_question_label.pack()
        self.add_question_entry = tk.Entry(self)
        self.add_question_entry.pack()

        add_answer_label = tk.Label(self, text="New Answer:")
        add_answer_label.pack()
        self.add_answer_entry = tk.Entry(self)
        self.add_answer_entry.pack()

        add_flashcard_button = tk.Button(self, text="Add Flashcard", command=self.add_flashcard)
        add_flashcard_button.pack()

        # Edit quiz name section
        edit_quiz_name_label = tk.Label(self, text="Edit Quiz Name:")
        edit_quiz_name_label.pack()
        self.edit_quiz_name_entry = tk.Entry(self)
        self.edit_quiz_name_entry.pack()

        edit_quiz_name_button = tk.Button(self, text="Save New Name", command=self.edit_quiz_name)
        edit_quiz_name_button.pack()

        # Delete quiz button
        delete_quiz_button = tk.Button(self, text="Delete Quiz", command=self.delete_quiz)
        delete_quiz_button.pack()

        # Back button
        back_button = tk.Button(self, text="Back", command=self.back_to_quiz)
        back_button.pack()

        # Debugging step: Print to check widget initialization
        print("Debug: add_question_entry initialized?", self.add_question_entry)
        print("Debug: edit_quiz_name_entry initialized?", self.edit_quiz_name_entry)

    def add_flashcard(self):

        # Debugging
        if not self.add_question_entry or not self.add_answer_entry:
            print("Error: Entries for adding flashcards are not initialized.")
            return

        question = self.add_question_entry.get().strip()
        answer = self.add_answer_entry.get().strip()
        if question and answer:
            self.flashcard_manager.add_flashcard(question, answer)
            messagebox.showinfo("Success", "Flashcard added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter both question and answer.")

    def edit_quiz_name(self):

        # Debugging
        if not self.edit_quiz_name_entry:
            print("Error: Entry for editing quiz name is not initialized.")
            return

        new_name = self.edit_quiz_name_entry.get().strip()
        if new_name:
            self.flashcard_manager.edit_quiz_name(new_name)
            messagebox.showinfo("Success", "Quiz name updated!")
            self.switch_frame_callback('quiz', new_name)
        else:
            messagebox.showwarning("Input Error", "Please enter a new quiz name.")

    def delete_quiz(self):
        confirm = messagebox.askyesno("Confirm", "Are you sure want to delete this quiz?")
        if confirm:
            self.flashcard_manager.delete_quiz()
            messagebox.showinfo("Success", "Quiz deleted successfully!")
            self.switch_frame_callback('main')

    def back_to_quiz(self):
        self.switch_frame_callback('quiz', self.quiz_name)
