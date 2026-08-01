"""
Django development settings for FIGTR project.
"""

from .base import *  # noqa: F403
from .base import BASE_DIR, REST_FRAMEWORK

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Development database uses SQLite by default to allow running without PostgreSQL.
# Set USE_SQLITE=False and configure DB_* env vars to use PostgreSQL.
USE_SQLITE = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Django REST Framework - Development overrides
REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}
