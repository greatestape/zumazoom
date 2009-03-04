from django_evolution.mutations import *
from django.db import models

MUTATIONS = [
    RenameField('BlogPost', 'preview', 'raw_preview'),
]
