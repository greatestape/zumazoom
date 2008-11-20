import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

class BlogPost(models.Model):
    """A simple blog post"""
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique_for_date='pub_date')
    pub_date = models.DateTimeField(_('pub_date'), default=datetime.datetime.now)
    body = models.TextField(_('body'), blank=True)

    class Meta:
        verbose_name = _('blog post')
        verbose_name_plural = _('blog posts')
        ordering = ('-pub_date',)

    def __unicode__(self):
        return _('%(title)s (Posted: %(pub_date)s)') % {
                    'title': self.title,
                    'pub_date': self.pub_date.strftime('%B %d, %Y')
                    }
