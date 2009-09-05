
from south.db import db
from django.db import models
from attachments.models import *
from attachments.models import _get_attachment_file_path

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Attachment.title'
        db.add_column('attachments_attachment', 'title', models.CharField(_('Title'), max_length=255, blank=True, default=""), keep_default=False)
        
        # Adding field 'Attachment.url'
        db.add_column('attachments_attachment', 'url', models.URLField(_('URL'), null=True, verify_exists=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Attachment.title'
        db.delete_column('attachments_attachment', 'title')
        
        # Deleting field 'Attachment.url'
        db.delete_column('attachments_attachment', 'url')
        
    
    
    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label','model'),)", 'db_table': "'django_content_type'"},
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'attachments.attachment': {
            'attached_file': ('models.FileField', ["_('attached_file')"], {'null': 'True', 'upload_to': '_get_attachment_file_path', 'blank': 'True'}),
            'content_type': ('models.ForeignKey', ['ContentType'], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('models.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('models.CharField', ["_('Title')"], {'max_length': '255', 'blank': 'True'}),
            'url': ('models.URLField', ["_('URL')"], {'null': 'True', 'verify_exists': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['attachments']
