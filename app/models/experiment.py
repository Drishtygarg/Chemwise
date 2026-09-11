"""
Experiment model.

Represents a saved record of a user running an experiment: which
chemicals they chose, which reaction result applied, and when. Used
for the History feature added in a later step.
"""
from datetime import datetime

from app.extensions import db


class Experiment(db.Model):
    __tablename__ = "experiments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    chemical_a_id = db.Column(db.Integer, db.ForeignKey("chemicals.id"), nullable=False)
    chemical_b_id = db.Column(db.Integer, db.ForeignKey("chemicals.id"), nullable=False)
    reaction_id = db.Column(db.Integer, db.ForeignKey("reactions.id"), nullable=True)
    observations = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User")
    chemical_a = db.relationship("Chemical", foreign_keys=[chemical_a_id])
    chemical_b = db.relationship("Chemical", foreign_keys=[chemical_b_id])
    reaction = db.relationship("Reaction")

    def __repr__(self):
        return f"<Experiment user={self.user_id} reaction={self.reaction_id}>"
