"""
Central configuration for ChemWise.

Values come from environment variables (loaded from .env in development)
so nothing sensitive or environment-specific is hard-coded in source.

Step 1 scope: only the minimum settings needed to boot Flask. Database,
Gemini/AI, and other feature-specific settings will be added in the
steps that introduce those features, not here.
"""
import os

from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Settings shared by all environments."""
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_ENV = os.environ.get("FLASK_ENV", "production")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///chemwise.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


def get_config():
    """Return the config class matching FLASK_ENV."""
    env = os.environ.get("FLASK_ENV", "production")
    if env == "development":
        return DevelopmentConfig
    return ProductionConfig
