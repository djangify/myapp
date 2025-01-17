from pathlib import Path
import environ
import os
import sys
from environ import Env
import pymysql

pymysql.install_as_MySQLdb()

# Initialize environment variables
env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
logs_dir = BASE_DIR / "logs"

# Load the .env file
ENV_FILE = ".env"
environ.Env.read_env(os.path.join(BASE_DIR, ENV_FILE))

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["127.0.0.1"])

# Configure CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="your-secret-key-here")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'core',
    'portfolio',
    'news',
    'shop',
    'contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'myapp.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  
        "APP_DIRS": True,  
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = 'myapp.wsgi.application'


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": env("DATABASE_HOST", default="127.0.0.1"),
        "PORT": env("DATABASE_PORT", default="3306"),
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            "use_unicode": True,
            "connect_timeout": 10,
            "autocommit": True,
        },
    },
}

# Security Settings
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True
X_FRAME_OPTIONS = 'SAMEORIGIN'

# IP Rate limiting settings
IP_RATE_LIMIT_MAX_ATTEMPTS = 20  # Maximum attempts per IP
IP_RATE_LIMIT_TIMEOUT = 300  # Reset after 5 minutes (in seconds)

# Session and CSRF settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# WhiteNoise configuration (if you're using WhiteNoise)
WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False

# Media File Headers
MEDIA_FILE_SERVE_HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Cache-Control': 'no-cache, must-revalidate'
}

# Cache Control Headers for Media Files
MEDIA_FILE_STORAGE_HEADERS = {
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0'
}

# File Permissions (if you're handling file uploads)
FILE_UPLOAD_PERMISSIONS = 0o644
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755


# Media settings
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# CKEditor settings
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True
CKEDITOR_JQUERY_URL = None
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename_generator'

CKEDITOR_UPLOAD_PATH = "uploads/ckeditor/"
CKEDITOR_ALLOW_NONIMAGE_FILES = True
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "height": 300,
        "width": "100%",
        "removePlugins": "stylesheetparser",
        "extraPlugins": ",".join(
            [
                "uploadimage",
                "image2",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath",
            ]
        ),
        "uploadUrl": "/ckeditor/upload/",
        "filebrowserUploadUrl": "/ckeditor/upload/",
        "filebrowserBrowseUrl": "/ckeditor/browse/",
        "contentsCss": [
            "p { margin: 0.5em 0; }",
            "h1, h2, h3, h4, h5, h6 { font-family: 'Lato', sans-serif; }",
        ],
        "enterMode": 2,
        "shiftEnterMode": 1,
        "format_tags": "p;h1;h2;h3;pre",
        "removeDialogTabs": "image:advanced;link:advanced",
        "stylesSet": [
            {
                "name": "Paragraph",
                "element": "p",
                "attributes": {"style": "margin: 0.5em 0;"},
            },
            {
                "name": "Heading 1",
                "element": "h1",
                "attributes": {"style": "font-family: 'Lato', sans-serif;"},
            },
            {
                "name": "Heading 2",
                "element": "h2",
                "attributes": {"style": "font-family: 'Lato', sans-serif;"},
            },
            {
                "name": "Heading 3",
                "element": "h3",
                "attributes": {"style": "font-family: 'Lato', sans-serif;"},
            },
        ],
    },
}

COLLECT_STATIC = "collectstatic" in sys.argv

SITE_ID = 1

SITE_URL = "https://www.djangify.com"




# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Add this logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))