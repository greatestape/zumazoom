import os, sys


sys.path.append('/home/zumazoom/live/site/')
sys.path.append('/home/zumazoom/live/site/zumazoom')
sys.path.append('/home/zumazoom/live/site/lib')

import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'zumazoom.settings'
application = django.core.handlers.wsgi.WSGIHandler()