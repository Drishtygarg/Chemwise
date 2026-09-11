"""
Flask extension instances live here (e.g. SQLAlchemy, Migrate) so they
can be imported without circular-import issues between app/__init__.py
and the models/routes that use them.

Step 2 scope: adds the SQLAlchemy instance used by all models. Kept
here (rather than in app/__init__.py) so models can import `db`
without triggering circular imports with the app factory.

Step 7 scope: adds the Flask-Login manager for session-based auth.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Please log in to run experiments."
