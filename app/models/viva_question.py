"""
VivaQuestion model.

One question within a VivaSession. answer_text/is_correct/feedback
stay null until the student submits an answer.
"""
from datetime import datetime

from app.extensions import db


class VivaQuestion(db.Model):
    __tablename__ = "viva_questions"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey("viva_sessions.id"), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    answer_text = db.Column(db.Text)
    is_correct = db.Column(db.Boolean)
    feedback = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<VivaQuestion session={self.session_id} answered={self.answer_text is not None}>"
