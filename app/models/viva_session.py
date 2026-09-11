"""
VivaSession model.

Represents one AI-tutored viva (oral-exam-style Q&A) session tied to
a specific saved experiment. Gemini asks questions and evaluates
answers grounded in that experiment's already-confirmed reaction
data — it never re-decides the chemistry itself.
"""
from datetime import datetime

from app.extensions import db


class VivaSession(db.Model):
    __tablename__ = "viva_sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    experiment_id = db.Column(db.Integer, db.ForeignKey("experiments.id"), nullable=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User")
    experiment = db.relationship("Experiment")
    questions = db.relationship(
        "VivaQuestion", backref="session", order_by="VivaQuestion.created_at"
    )

    def __repr__(self):
        return f"<VivaSession user={self.user_id} experiment={self.experiment_id}>"
