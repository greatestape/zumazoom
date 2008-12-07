from django_evolution.mutations import *
from django.db import models

MUTATIONS = [
    AddField('BlogPost', 'category', models.ForeignKey, null=True, related_model='blog.Category')
]
