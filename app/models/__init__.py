"""
Importing each model here ensures they register with SQLAlchemy's
metadata when `app.models` is imported, so db.create_all() finds them.
"""
from app.models.user import User
from app.models.chemical import Chemical
from app.models.reaction import Reaction
from app.models.experiment import Experiment
from app.models.viva_session import VivaSession
from app.models.viva_question import VivaQuestion

__all__ = ["User", "Chemical", "Reaction", "Experiment", "VivaSession", "VivaQuestion"]
