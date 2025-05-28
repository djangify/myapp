import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings.production')
# Ensure the settings module is set to production

application = get_wsgi_application()
