from datetime import datetime

class Form:
    def __init__(self, title, description, questions):
        self.title = title
        self.description = description
        self.questions = questions
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "questions": self.questions,
            "createdAt": self.created_at
        }
