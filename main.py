from DatabaseManager import DatabaseManager
from FlashcardManager import FlashcardManager
from FlashcardApp import FlashcardApp
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    db_manager = DatabaseManager()
    flashcard_manager = FlashcardManager(db_manager)
    app = FlashcardApp(root, flashcard_manager)
    root.mainloop()
