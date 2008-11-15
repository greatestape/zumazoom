# Django project site specific settings
# All non site specific settings should go into the settings.py file

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = '@$5+z4lcu+6qek5o9$s)t82x&xw21cs-cz)hw)h28^&70v*)df'

ADMINS = (
    ('Sam Bull', 'sam@pocketuniverse.ca'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'localdev.db'

TIME_ZONE = 'Canada/Eastern'

ROOT_URLCONF = 'dev_urls'

INTERNAL_IPS = ('127.0.0.1', )

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
