from MainFrame import MainFrame
from QuizFrame import QuizFrame
from FlashcardManagementFrame import FlashcardManagementFrame
from QuizPlayFrame import QuizPlayFrame


class FrameManager:
    def __init__(self, root, flashcard_manager):
        self.root = root
        self.flashcard_manager = flashcard_manager
        self.current_frame = None
        self.show_frame('main')

    def show_frame(self, frame_type, quiz_name=None):
        if self.current_frame:
            self.current_frame.destroy()

        if frame_type == 'main':
            self.current_frame = MainFrame(self.root, self.flashcard_manager, self.show_frame)
        if frame_type == 'quiz':
            self.current_frame = QuizFrame(self.root, self.flashcard_manager, quiz_name, self.show_frame)
        if frame_type == 'edit':
            self.current_frame = FlashcardManagementFrame(self.root, self.flashcard_manager, quiz_name, self.show_frame)
        if frame_type == 'play':
            self.current_frame = QuizPlayFrame(self.root, self.flashcard_manager, quiz_name, self.show_frame)

        self.current_frame.pack()
