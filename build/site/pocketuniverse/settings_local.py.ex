# Django project site specific settings
# All non site specific settings should go into the settings.py file
# Copy this file as settings_local.py and adjust it to your site.
# The settings_local.py contains only site specific information and should not
# be part of the svn repository of the project. It should be part of the
# hosting svn repository.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
# You can generate a new one with ./manage.py generate_secret_key
#TODO
SECRET_KEY = ''

ADMINS = (
    #('Bonefish Grill Team', 'powerwise_team@trapeze.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3' # change for production
DATABASE_NAME = 'localdev.db'
#DATABASE_USER = 'TODO on production'
#DATABASE_PASSWORD = 'TODO on production'
#DATABASE_HOST = '127.0.0.1' # Needed for PostgreSQL

TIME_ZONE = 'Canada/Eastern'

ROOT_URLCONF = 'dev_urls' #TODO: remove this on production

INTERNAL_IPS = ('127.0.0.1', )

# TODO: MEDIA_URL needs to be a full URL on production
# in case some media (images) are embedded in another site
MEDIA_URL = '/media/' #TODO: on production (full URL to the media server)

ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

# Uncomment the following lines to disable the project
# specific templates, css, images, ...
#import os
#
#PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
#
#MEDIA_ROOT = os.path.join(PROJECT_PATH, 'dev_media/')
#
#TEMPLATE_DIRS = (
#    os.path.join(PROJECT_PATH, 'dev_templates/'),
#)

