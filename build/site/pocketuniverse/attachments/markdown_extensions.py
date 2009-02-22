"""
Attachments extension for Markdown

This module provides an extension to markdown for embedding attachments into
markdown text.

Markdown usage:

    [attach:<filename>]
    [attach:<filename>|<template>] or
    [attach:(<content_type_id>,<object_id>)<filename>] or
    [attach:(<content_type_id>,<object_id>)<filename>|<template>)]

"""
import os.path
import re

from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string

import markdown

from attachments.models import Attachment

ATTACH_PATTERN = re.compile(r'\[attach:(?:\((\d+?),(\d+?)\))?(.+?)(?:\|(.+?))??\]')


class AttachmentPreprocessor(markdown.TextPreprocessor):

    def __init__(self, attachment_template):
        self.attachment_template = attachment_template

    def run(self, text):
        def repl(m):
            try:
                attachment_qs = Attachment.objects.all()
                content_type_id = m.group(1)
                object_id = m.group(2)
                if content_type_id and object_id:
                    attachment_qs = attachment_qs.filter(
                            content_type__id=content_type_id,
                            object_id=object_id)
                attachment = attachment_qs.get(attached_file__endswith=u'/%s' % m.group(3))
            except (Attachment.DoesNotExist, Attachment.MultipleObjectsReturned):
                return ''
            else:
                template_base, template_ext = os.path.splitext(self.attachment_template)
                templates = []
                style = m.group(4)
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
        return ATTACH_PATTERN.sub(
            repl, text)


class AttachmentsExtension(markdown.Extension):
    config = {'t' : [
            'attachments/_inline.html', 
            'The template to use when rendering an attachment'
            ]}

    def __init__(self, configs):
        for (param, value) in configs:
            self.setConfig(param, value)

    def extendMarkdown(self, md, md_globals):
        md.textPreprocessors.insert(0, AttachmentPreprocessor(self.getConfig('t')))


def connect_attachments(object, text):
    content_type = ContentType.objects.get_for_model(object)
    def repl(m):
        if m.group(1) and m.group(2):
            return m.group(0)
        else:
            return '[attach:(%s,%s)%s%s]' % (
                    content_type.pk,
                    object.pk,
                    m.group(3),
                    m.group(4) and '|%s' % m.group(4) or '',
                    )
    return ATTACH_PATTERN.sub(repl, text)