import os.path

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


FILE_TYPES = {
    'image': set(['jpg', 'jpeg', 'png', 'gif']),
}

FILE_TYPES_LOOKUP = {}
for ftype, extensions in FILE_TYPES.items():
    for ext in extensions:
        FILE_TYPES_LOOKUP['.%s' % ext] = ftype


def _get_attachment_file_path(attachment, filename):
    return 'managed/%s/%s/%s/%s' % (
        attachment.content_type.app_label,
        attachment.content_type.model,
        attachment.object_id,
        filename
        )


class Attachment(models.Model):
    """A file attached to another object"""
    attached_file = models.FileField(_('File'), null=True, blank=True, upload_to=_get_attachment_file_path)
    url = models.URLField(_('URL'), blank=True, null=True, verify_exists=True)
    title = models.CharField(_('Title'), blank=True, max_length=255)
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    target_object = generic.GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = _('attachment')
        verbose_name_plural = _('attachments')

    def __unicode__(self):
        return _('%(file)s attached to %(obj)s') % {
            'file': self.attached_file.name.rsplit('/',1)[1],
            'obj': self.target_object,
            }

    @property
    def file_type(self):
        filename, ext = os.path.splitext(self.attached_file.name)
        return FILE_TYPES_LOOKUP.get(ext, 'other')

    @property
    def filename(self):
        return os.path.split(self.attached_file.name)[1]
