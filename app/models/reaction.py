"""
Reaction model.

Stores deterministic, pre-validated reaction data for a pair of
chemicals. This table is the chemistry "source of truth" per the
spec — the Reaction Engine (added in a later step) reads from here.
Gemini never writes to or decides the contents of this table.
"""
from app.extensions import db


class Reaction(db.Model):
    __tablename__ = "reactions"

    id = db.Column(db.Integer, primary_key=True)
    chemical_a_id = db.Column(db.Integer, db.ForeignKey("chemicals.id"), nullable=False)
    chemical_b_id = db.Column(db.Integer, db.ForeignKey("chemicals.id"), nullable=False)
    is_valid = db.Column(db.Boolean, default=False, nullable=False)
    reaction_type = db.Column(db.String(60))
    equation = db.Column(db.String(255))
    products = db.Column(db.Text)
    observations = db.Column(db.Text)
    safety_level = db.Column(db.String(30))

    chemical_a = db.relationship("Chemical", foreign_keys=[chemical_a_id])
    chemical_b = db.relationship("Chemical", foreign_keys=[chemical_b_id])

    def __repr__(self):
        return f"<Reaction {self.chemical_a_id}+{self.chemical_b_id}>"
