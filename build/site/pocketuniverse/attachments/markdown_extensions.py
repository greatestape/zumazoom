"""
Attachments extension for Markdown

This module provides an extension to markdown for embedding attachments into
markdown text.

Markdown usage:

    [attach:<filename>]

"""
import os.path
import re

from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string

import markdown

from attachments.models import Attachment


class AttachmentPreprocessor(markdown.TextPreprocessor):

    pattern = re.compile(r'\[attach:(.+?)(?:\|(.+?))??\]')

    def __init__(self, content_type_id, object_id, attachment_template):
        print content_type_id, object_id, attachment_template
        qs = Attachment.objects.all()
        if content_type_id:
            qs = qs.filter(content_type__id=content_type_id)
        if object_id:
            qs = qs.filter(object_id=object_id)
        self.attachment_qs = qs
        self.attachment_template = attachment_template

    def run(self, text):
        def repl(m):
            try:
                attachment = self.attachment_qs.get(attached_file__endswith=u'/%s' % m.group(1))
            except (Attachment.DoesNotExist, Attachment.MultipleObjectsReturned):
                return ''
            else:
                template_base, template_ext = os.path.splitext(self.attachment_template)
                templates = []
                style = m.group(2)
                if style:
                    templates.append('%s-%s-%s%s' % ( # i.e. template-image-floatright.html
                        template_base,
                        attachment.file_type,
                        style,
                        template_ext,
                        ))
                    templates.append('%s-%s%s' % ( # i.e. template-floatright.html
                        template_base,
                        style,
                        template_ext,
                        ))
                templates.append('%s-%s%s' % ( # i.e. template-image.html
                    template_base,
                    attachment.file_type,
                    template_ext,
                    ))
                templates.append(self.attachment_template) # i.e. template.html
                context = {'attachment': attachment,}
                return render_to_string(templates, context)
        return self.pattern.sub(
            repl, text)


class AttachmentsExtension(markdown.Extension):
    config = {'content_type_id' : [None, 'The id of the ContentType of the object the attachments are attached to'],
              'object_id' : [None, 'The id of the object the attachments are attached to'],
              'template' : ['attachments/_inline.html', 'The template to use when rendering an attachment'] }

    def __init__(self, configs):
        for (param, value) in configs:
            self.setConfig(param, value)

    def extendMarkdown(self, md, md_globals):
        md.textPreprocessors.insert(0, AttachmentPreprocessor(
            self.getConfig('content_type_id'),
            self.getConfig('object_id'),
            self.getConfig('template')
            ))
