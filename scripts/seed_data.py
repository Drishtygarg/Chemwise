"""
Seed script for ChemWise.

Loads app/data/chemicals.json into the Chemical table, then resolves
the formula pairs in app/data/reactions.json into Reaction rows.
Idempotent: safe to run multiple times, will not create duplicates.

Usage:
    python scripts/seed_data.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.extensions import db
from app.models import Chemical, Reaction

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app", "data")


def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), encoding="utf-8") as f:
        return json.load(f)


def seed_chemicals():
    chemicals_data = load_json("chemicals.json")
    created = 0
    for entry in chemicals_data:
        existing = Chemical.query.filter_by(formula=entry["formula"]).first()
        if existing:
            continue
        db.session.add(Chemical(**entry))
        created += 1
    db.session.commit()
    print(f"Chemicals: {created} created, {len(chemicals_data) - created} already existed.")


def seed_reactions():
    reactions_data = load_json("reactions.json")
    created = 0
    skipped_missing = 0
    for entry in reactions_data:
        chem_a = Chemical.query.filter_by(formula=entry["chemical_a_formula"]).first()
        chem_b = Chemical.query.filter_by(formula=entry["chemical_b_formula"]).first()
        if not chem_a or not chem_b:
            skipped_missing += 1
            continue

        existing = Reaction.query.filter(
            db.or_(
                db.and_(Reaction.chemical_a_id == chem_a.id, Reaction.chemical_b_id == chem_b.id),
                db.and_(Reaction.chemical_a_id == chem_b.id, Reaction.chemical_b_id == chem_a.id),
            )
        ).first()
        if existing:
            continue

        db.session.add(Reaction(
            chemical_a_id=chem_a.id,
            chemical_b_id=chem_b.id,
            is_valid=True,
            reaction_type=entry["reaction_type"],
            equation=entry["equation"],
            products=entry["products"],
            observations=entry["observations"],
            safety_level=entry["safety_level"],
        ))
        created += 1
    db.session.commit()
    print(f"Reactions: {created} created, {skipped_missing} skipped (missing chemical).")


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_chemicals()
        seed_reactions()
