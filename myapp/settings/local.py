"""
Local development settings for [Project Name].
"""

from .base import *
import os
import environ

# Load .env.local
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env.local"))

SITE_URL = env("SITE_URL", default="http://localhost:8000")

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
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Stripe settings
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY", default="pk_test_placeholder")
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY", default="sk_test_placeholder")
STRIPE_WEBHOOK_SECRET = env("STRIPE_WEBHOOK_SECRET", default="whsec_placeholder")
CART_SESSION_ID = "cart"
