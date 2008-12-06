from django.shortcuts import get_object_or_404
from django.views.generic import simple, date_based

from blog.models import BlogPost, Category

def home(request):
    return date_based.archive_index(
        request,
        BlogPost.objects.all(),
        date_field='pub_date',
        template_name='blog/home.html',
        template_object_name='latest_blogposts')


def post_detail(request, year, month, day, slug):
    return date_based.object_detail(
        request,
        year=year,
        month=month, month_format="%B",
        day=day,
        slug=slug, slug_field='slug',
        date_field='pub_date',
        queryset=BlogPost.objects.all(),
        template_object_name='blogpost'
        )


def archive_month(request, year, month):
    return date_based.archive_month(
        request,
        year=year,
        month=month, month_format="%B",
        date_field='pub_date',
        queryset=BlogPost.objects.all(),
        template_object_name='blogpost'
        )

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return date_based.archive_index(
        request,
        category.blogpost_set.all(),
        date_field='pub_date',
        template_name='blog/category_detail.html',
        template_object_name='latest_blogposts')