import sqlite3


class DatabaseManager:
    def __init__(self, db_name='flashcards.db'):
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        # Create the quizzes table
        c.execute('''CREATE TABLE IF NOT EXISTS quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT UNIQUE NOT NULL)''')

        # Create the flashcards table
        c.execute('''CREATE TABLE IF NOT EXISTS flashcards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    answered_correctly BOOLEAN DEFAULT 0,
                    quiz_id INTEGER NOT NULL,
                    FOREIGN KEY (quiz_id) REFERENCES quizzes(id))''')

        conn.commit()
        conn.close()

    def add_quiz(self, quiz_name):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        try:
            c.execute("INSERT INTO quizzes (name) VALUES (?)", (quiz_name,))
            conn.commit()
        except sqlite3.IntegrityError:
            print(f"A quiz named '{quiz_name}' already exists.")
        finally:
            conn.close()

    def get_quizzes(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT id, name FROM quizzes")
        quizzes = c.fetchall()
        conn.close()
        return quizzes

    def add_flashcard(self, question, answer, quiz_id):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO flashcards (question, answer, quiz_id) VALUES (?, ?, ?)", (question, answer, quiz_id))
        conn.commit()
        conn.close()

    def get_flashcards(self, quiz_id):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT id, question, answer, answered_correctly FROM flashcards WHERE answered_correctly = 0 AND "
                  "quiz_id = ?", (quiz_id,))
        flashcards = c.fetchall()
        conn.close()
        return flashcards

    def mark_as_answered(self, card_id):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("UPDATE flashcards SET answered_correctly = 1 WHERE id = ?", (card_id,))
        conn.commit()
        conn.close()
