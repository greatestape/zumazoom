from attachments.models import Attachment
from django.contrib.contenttypes import generic


class AttachmentInline(generic.GenericStackedInline):
    model = Attachment
    max_num = 1
    extra = 1

