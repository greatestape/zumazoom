# Django project settings file
# This file should be part of the svn repository of the project and should not
# contains any site-specific information.
# site-specific information (database name/login/password for example) should be
# in the settings_local.py file and should not be added to the svn repository

import os

SITE_ID = 1

USE_I18N = True

LANGUAGE_CODE = 'en-ca'

gettext = lambda s: s
LANGUAGES = (('en-ca', gettext('English')),)

AKISMET_API_KEY = '21adb0516170'

BLOG_AUTHOR_ID = 1

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'


PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',

    'django_extensions',
    'sorl.thumbnail',
    'south',
    'tagging',

    'attachments',
    'blog',
)

# import local settings overriding the defaults
try:
    from settings_local import *
except ImportError:
    try:
        from mod_python import apache
        apache.log_error( "local settings not available", apache.APLOG_NOTICE )
    except ImportError:
        import sys
        sys.stderr.write( "local settings not available\n" )

