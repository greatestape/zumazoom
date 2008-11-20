import os, sys


sys.path.append('/home/sam/projects/pocketuniverse/build/site')
sys.path.append('/home/sam/projects/pocketuniverse/build/site/pocketuniverse')
sys.path.append('/home/sam/projects/pocketuniverse/build/site/lib')

import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'pocketuniverse.settings'
application = django.core.handlers.wsgi.WSGIHandler()