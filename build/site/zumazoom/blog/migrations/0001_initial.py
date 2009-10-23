
from south.db import db
from django.db import models
from blog.models import *

class Migration:
    def forwards(self, orm):
        # Adding model 'BlogPost'
        db.create_table('blog_blogpost', (
            ('category', models.ForeignKey(orm.Category, null=True, verbose_name=_('category'), blank=True)),
            ('raw_preview', models.TextField(_('preview'), blank=True)),
            ('title', models.CharField(_('title'), max_length=100)),
            ('raw_body', models.TextField(_('body'), blank=True)),
            ('slug', models.SlugField(_('slug'), max_length=100, unique_for_date='pub_date')),
            ('id', models.AutoField(primary_key=True)),
            ('pub_date', models.DateTimeField(_('pub_date'), default=datetime.datetime.now)),
            ('public', models.BooleanField(_('public'), default=False)),
        ))
        db.send_create_signal('blog', ['BlogPost'])

        # Adding model 'Category'
        db.create_table('blog_category', (
            ('slug', models.SlugField(_('slug'), max_length=100)),
            ('id', models.AutoField(primary_key=True)),
            ('weight', models.IntegerField(_('weight'), default=0)),
            ('name', models.CharField(_('name'), max_length=100)),
        ))
        db.send_create_signal('blog', ['Category'])

    def backwards(self, orm):
        # Deleting model 'BlogPost'
        db.delete_table('blog_blogpost')

        # Deleting model 'Category'
        db.delete_table('blog_category')

    models = {
        'blog.blogpost': {
            'Meta': {'ordering': "('-pub_date',)", 'get_latest_by': "'pub_date'"},
            'category': ('models.ForeignKey', ['Category'], {'null': 'True', 'verbose_name': "_('category')", 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('models.DateTimeField', ["_('pub_date')"], {'default': 'datetime.datetime.now'}),
            'public': ('models.BooleanField', ["_('public')"], {'default': 'False'}),
            'raw_body': ('models.TextField', ["_('body')"], {'blank': 'True'}),
            'raw_preview': ('models.TextField', ["_('preview')"], {'blank': 'True'}),
            'slug': ('models.SlugField', ["_('slug')"], {'max_length': '100', 'unique_for_date': "'pub_date'"}),
            'title': ('models.CharField', ["_('title')"], {'max_length': '100'})
        },
        'blog.category': {
            'Meta': {'ordering': "('weight','name')"},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', ["_('name')"], {'max_length': '100'}),
            'slug': ('models.SlugField', ["_('slug')"], {'max_length': '100'}),
            'weight': ('models.IntegerField', ["_('weight')"], {'default': '0'})
        }
    }

    complete_apps = ['blog']
