from django_evolution.mutations import *
from django.db import models

MUTATIONS = [
    AddField('BlogPost', 'preview', models.TextField, initial='')
]