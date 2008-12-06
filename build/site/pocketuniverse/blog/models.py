import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    """A category of blog post"""
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100)
    weight = models.IntegerField(_('weight'), default=0)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('weight', 'name')

    def __unicode__(self):
        return self.name


class BlogPost(models.Model):
    """A simple blog post"""
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100, unique_for_date='pub_date')
    pub_date = models.DateTimeField(_('pub_date'), default=datetime.datetime.now)
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name=_('category'))
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

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_detail', (), {
            'year': self.pub_date.year,
            'month': self.pub_date.strftime('%B').lower(),
            'day': self.pub_date.day,
            'slug': self.slug,
            })
