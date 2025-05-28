"""
Local development settings for [Project Name].
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Override database settings completely - hardcoded for local PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "djangify_myapp_db",  # From PostgreSQL setup
        "USER": "myapp_user",  # From PostgreSQL setup
        "PASSWORD": "s70b8KSC2epC349D",  # From PostgreSQL setup
        "HOST": "127.0.0.1",
        "PORT": "5433",
    }
}

# Local development settings
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False

SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True

# Email backend for development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
