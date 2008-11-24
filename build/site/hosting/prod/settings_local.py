# Django project site specific settings
# All non site specific settings should go into the settings.py file

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = '@$5+z4lcu+6qek5o9$s)t82x&xw21cs-cz)hw)h28^&70v*)df'

ADMINS = (
    ('Sam Bull', 'sam@pocketuniverse.ca'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_HOST = 'localhost'
DATABASE_NAME = 'pocketuniverse'
DATABASE_USER = 'pocketuniverse'
DATABASE_PASSWORD = 'kloul7ad7yur'

TIME_ZONE = 'Canada/Eastern'

ROOT_URLCONF = 'pocketuniverse.urls'

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

PREPEND_WWW = True
