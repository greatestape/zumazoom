from django.views.generic import simple, date_based

from blog.models import BlogPost

def home(request):
    blogpost_list = BlogPost.objects.all()
    return simple.direct_to_template(request, 'blog/home.html',
                                     {'blogpost_list': blogpost_list})


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
