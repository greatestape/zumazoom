
from south.db import db
from django.db import models
from attachments.models import *
from attachments.models import _get_attachment_file_path

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Attachment'
        db.create_table('attachments_attachment', (
            ('attached_file', models.FileField(_('attached_file'), null=True, upload_to=_get_attachment_file_path, blank=True)),
            ('id', models.AutoField(primary_key=True)),
            ('content_type', models.ForeignKey(orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', models.PositiveIntegerField(null=True, blank=True)),
        ))
        db.send_create_signal('attachments', ['Attachment'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Attachment'
        db.delete_table('attachments_attachment')
        
    
    
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
            'object_id': ('models.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['attachments']
