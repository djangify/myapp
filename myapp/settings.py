from pathlib import Path
import environ
import os
import sys
import stripe
from environ import Env
import pymysql 

pymysql.install_as_MySQLdb()

# Initialize environment variables
env = environ.Env()

SITE_ID = 1

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
logs_dir = BASE_DIR / "logs"

# Load the .env file
ENV_FILE = ".env"
environ.Env.read_env(os.path.join(BASE_DIR, ENV_FILE))

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'localhost:8000']

# CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:8000",
]


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
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'ckeditor',
    'ckeditor_uploader',
    'shop',
    'core',
    'portfolio',
    'news',
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


# Cache Control Headers for Media Files
MEDIA_FILE_STORAGE_HEADERS = {
    'Cache-Control': 'no-cache, no-store, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0'
}


# Media settings
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Ensure media directory exists
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
# Static files configuration
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# CKEditor settings
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True
CKEDITOR_JQUERY_URL = None


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

# Shop App Settings
STRIPE_PUBLIC_KEY = env('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = env('STRIPE_WEBHOOK_SECRET')

# Initialize Stripe
stripe.api_key = STRIPE_SECRET_KEY


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
