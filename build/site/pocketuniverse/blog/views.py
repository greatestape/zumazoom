from django.views.generic import simple, date_based

from blog.models import BlogPost

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
