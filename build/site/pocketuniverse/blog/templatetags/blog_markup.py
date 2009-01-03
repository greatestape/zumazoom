from django import template
from django.contrib.contenttypes.models import ContentType

import markdown

register = template.Library()


@register.simple_tag
def format_body(blogpost, attachment_template=None):
    return _format_field(blogpost, 'raw_body', attachment_template)


@register.simple_tag
def format_preview(blogpost, attachment_template=None):
    return _format_field(blogpost, 'raw_preview', attachment_template)


def _format_field(blogpost, field, attachment_template=None):
    if not attachment_template:
        attachment_template = 'blog/_blogpost_attachment.html'
    md = markdown.Markdown(
        getattr(blogpost, field),
        extensions=['pygments', 'attachments'],
        extension_configs={'attachments': [
            ('content_type_id', ContentType.objects.get_for_model(blogpost).pk),
            ('object_id', blogpost.pk),
            ('template', attachment_template),
            ]}
        )
    return md.convert()