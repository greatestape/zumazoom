# Django project site specific settings
# All non site specific settings should go into the settings.py file

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = '*obiqcq259mi^urkrej-ltp5v23p54lrs$j+n)qq&+52hqq6q!'

ADMINS = (
    ('Dael Stewart', 'sookaa@gmail.com'),
    ('Sam Bull', 'osirius@gmail.com'),
    ('Taylan Pince', 'taylanpince@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_HOST = 'localhost'
DATABASE_NAME = 'zumazoom'
DATABASE_USER = 'zumazoom'
DATABASE_PASSWORD = 'wav-orc-it-vod-u'

TIME_ZONE = 'America/Toronto'

ROOT_URLCONF = 'zumazoom.urls'

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

PREPEND_WWW = True
