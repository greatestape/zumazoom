from django import template
from django.conf import settings
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe

from markdown import Markdown

from pg_md_processor import CodeBlockPreprocessor

register = template.Library()

@register.filter
def markdown(value, arg=''):
    """
    Runs Markdown over a given value, optionally using various
    extensions python-markdown supports.

    Syntax::

        {{ value|markdown:"extension1_name,extension2_name..." }}

    To enable safe mode, which strips raw HTML and only returns HTML
    generated by actual Markdown syntax, pass "safe" as the first
    extension in the list.

    If the version of Markdown in use does not support extensions,
    they will be silently ignored.

    """
    extensions = [e for e in arg.split(",") if e]
    if len(extensions) > 0 and extensions[0] == "safe":
        extensions = extensions[1:]
        safe_mode = True
    else:
        safe_mode = False

    return mark_safe(_pygmented_markdown(force_unicode(value), extensions, safe_mode=safe_mode))
markdown.is_safe = True

def _pygmented_markdown(text,
             extensions = [],
             safe_mode = False):

    extension_names = []
    extension_configs = {}

    for ext in extensions:
        pos = ext.find("(")
        if pos == -1:
            extension_names.append(ext)
        else:
            name = ext[:pos]
            extension_names.append(name)
            pairs = [x.split("=") for x in ext[pos+1:-1].split(",")]
            configs = [(x.strip(), y.strip()) for (x, y) in pairs]
            extension_configs[name] = configs

    md = Markdown(extensions=extension_names,
                  extension_configs=extension_configs,
                  safe_mode = safe_mode)

    md.textPreprocessors.insert(0, CodeBlockPreprocessor())

    return md.convert(text)
