"""
ChemWise application factory.

Step 1 scope: skeleton only. No models, no blueprints with real routes,
no database, no AI integration yet. Just a Flask app that boots and
responds to a health-check request.
"""
from flask import Flask

from app.config import get_config
from app.extensions import db, login_manager


def create_app():
    """Create and configure the Flask application instance."""
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )
    app.config.from_object(get_config())

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from app import models  # noqa: F401  (registers models with SQLAlchemy)
        db.create_all()

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.routes.chemicals import chemicals_bp
    from app.routes.experiment import experiment_bp
    from app.routes.auth import auth_bp
    from app.routes.ai import ai_bp
    from app.routes.report import report_bp
    from app.routes.viva import viva_bp
    from app.routes.periodic_table import periodic_bp
    from app.routes.faculty import faculty_bp
    app.register_blueprint(chemicals_bp)
    app.register_blueprint(experiment_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(ai_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(viva_bp)
    app.register_blueprint(periodic_bp)
    app.register_blueprint(faculty_bp)

    from flask import redirect, url_for

    @app.route("/")
    def home():
        return redirect(url_for("chemicals.library"))

    @app.route("/health")
    def health_check():
        return {"status": "ok", "service": "ChemWise", "message": "ChemWise is running"}

    return app

