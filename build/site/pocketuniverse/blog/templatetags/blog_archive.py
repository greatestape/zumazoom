from django import template
from django.conf import settings

from blog.models import BlogPost

register = template.Library()

@register.filter
def months_with_content(date_list):
    """
    Returns a list of months where there are blog posts within the year range
    provided.

    Syntax:

        {{ date_list|months_with_content }}

    """
    dates = []
    for year_date in date_list:
        dates += list(BlogPost.objects.filter(pub_date__year=year_date.year).dates('pub_date', 'month'))
    return dates


@register.filter
def has_posts_in_month(date):
    if not date:
        return False
    return BlogPost.objects.filter(pub_date__year=date.year, pub_date__month=date.month).count() > 0
