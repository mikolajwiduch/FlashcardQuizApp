import tkinter as tk


class FlashcardManagementFrame(tk.Frame):
    def __init__(self, parent, flashcard_manager, quiz_name, switch_frame_callback):
        super().__init__(parent)
        self.flashcard_manager = flashcard_manager
        self.quiz_name = quiz_name
        self.setup_gui()
        self.switch_frame_callback = switch_frame_callback

    def setup_gui(self):
        label = tk.Label(self, text=f"Editing {self.quiz_name}")
        label.pack()

        # Logic to add/edit flashcards will be here

        # Back button
        back_button = tk.Button(self, text="Back", command=self.back_to_quiz)
        back_button.pack()

    def back_to_quiz(self):
        self.switch_frame_callback('quiz', self.quiz_name)
