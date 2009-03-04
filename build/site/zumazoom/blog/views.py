from django.shortcuts import get_object_or_404
from django.views.generic import simple, date_based

from blog.models import BlogPost, Category

def home(request):
    return date_based.archive_index(
        request,
        BlogPost.objects.public_posts(),
        date_field='pub_date',
        template_name='blog/home.html',
        template_object_name='blogpost_list',
        extra_context={'preview': True}
        )


def post_detail(request, year, month, day, slug):
    if request.user.is_staff:
        queryset = BlogPost.objects.all()
    else:
        queryset = BlogPost.objects.public_posts()
    return date_based.object_detail(
        request,
        year=year,
        month=month, month_format="%B",
        day=day,
        slug=slug, slug_field='slug',
        date_field='pub_date',
        queryset=queryset,
        template_object_name='blogpost',
        )


def archive_month(request, year, month, category_slug=None):
    queryset = BlogPost.objects.public_posts()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        queryset = queryset.filter(category=category)
    else:
        category = None

    return date_based.archive_month(
        request,
        year=year,
        month=month, month_format="%B",
        date_field='pub_date',
        queryset=queryset,
        template_object_name='blogpost',
        extra_context={'category': category, 'preview': True}
        )


def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return date_based.archive_index(
        request,
        category.blogpost_set.public_posts(),
        date_field='pub_date',
        template_name='blog/category_detail.html',
        template_object_name='blogpost_list',
        extra_context={'category': category, 'preview': True},
        )
