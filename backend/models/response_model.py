from datetime import datetime

class Response:
    def __init__(self, form_id, answers, client_id):
        self.form_id = form_id
        self.answers = answers
        self.client_id = client_id
        self.submitted_at = datetime.utcnow()

    def to_dict(self):
        return {
            "formId": self.form_id,
            "answers": self.answers,
            "clientId": self.client_id,
            "submittedAt": self.submitted_at
        }
