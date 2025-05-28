import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS
ALLOWED_HOSTS = [
    'djangify.corrisonapi.com',
    'djangify.com',  
    'www.djangify.com',
    'news.djangify.com', 
    'tracker.djangify.com',
    '.djangify.com',
    '65.108.89.200',
    'localhost',
    '127.0.0.1',
]

# Database in base.py is already set up to use environment variables

# CORS settings
CORS_ALLOWED_ORIGINS = [
    'https://djangify.corrisonapi.com',
    'https://djangify.com',
    'https://www.djangify.com',
]

# CSRF Configuration
CSRF_TRUSTED_ORIGINS = [
    'https://djangify.corrisonapi.com',
    'https://djangify.com',
    'https://www.djangify.com',
    'https://65.108.89.200',
    'http://localhost',
    'http://127.0.0.1',
]

# CSRF Cookie Configuration
CSRF_COOKIE_SECURE = True

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False

SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True

# Security settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

# Email settings for production
EMAIL_HOST = env('EMAIL_HOST', default='')
EMAIL_PORT = env('EMAIL_PORT', default=587)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = env('EMAIL_USE_TLS', default=True)
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='noreply@corrisonapi.com')

# Logging Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django-error.log'),
            'maxBytes': 10485760,  # 10 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'cors_file': {  # Add this handler
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/cors-debug.log'),
            'maxBytes': 10485760,
            'backupCount': 3,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'core': {  # Add this logger
            'handlers': ['cors_file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
# Ensure logs directory exists
log_dir = os.path.join(BASE_DIR, 'logs')
os.makedirs(log_dir, exist_ok=True)

# Load site-specific settings
try:
    from .site_settings import *
except ImportError:
    pass