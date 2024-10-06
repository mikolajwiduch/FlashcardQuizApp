class FlashcardManager:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.selected_quiz_id = None

    def create_quiz(self, quiz_name):
        self.db_manager.add_quiz(quiz_name)

    def select_quiz(self, quiz_name):
        quizzes = self.db_manager.get_quizzes()
        for quiz in quizzes:
            if quiz[1] == quiz_name:
                self.selected_quiz_id = quiz[0]
                return True
        return False

    def get_flashcards_for_quiz(self):
        if self.selected_quiz_id:
            return self.db_manager.get_flashcards(self.selected_quiz_id)
        else:
            raise ValueError("No quiz selected!")

    def add_flashcard(self, question, answer):
        if self.selected_quiz_id:
            self.db_manager.add_flashcard(question, answer, self.selected_quiz_id)
        else:
            raise ValueError("No quiz selected!")

    def mark_flashcard_answered(self, card_id):
        self.db_manager.mark_as_answered(card_id)
