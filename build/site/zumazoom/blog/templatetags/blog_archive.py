from django import template
from django.conf import settings

from blog.models import BlogPost, Category

register = template.Library()


@register.inclusion_tag('blog/_archive_nav.html')
def archive_nav(month=None, category=None):
    queryset = BlogPost.objects.all()
    if category:
        queryset = queryset.filter(category=category)
    return {'category': category,
            'active_month': month,
            'month_list': queryset.dates('pub_date', 'month')[::-1]
            }


@register.inclusion_tag('blog/_category_nav.html')
def category_nav(active_category=None):
    categories = Category.objects.all()
    return locals()

@register.filter
def has_posts_in_month(date):
    if not date:
        return False
    return BlogPost.objects.filter(pub_date__year=date.year, pub_date__month=date.month).count() > 0
