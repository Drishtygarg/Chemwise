"""
Chemical model.

Represents an entry in the controlled chemical catalog used for
experiment selection. Seed data is added in a later step, not here.
"""
from app.extensions import db


class Chemical(db.Model):
    __tablename__ = "chemicals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    formula = db.Column(db.String(60), nullable=False)
    category = db.Column(db.String(60))
    description = db.Column(db.Text)
    properties = db.Column(db.Text)
    safety_notes = db.Column(db.Text)

    def __repr__(self):
        return f"<Chemical {self.formula}>"
