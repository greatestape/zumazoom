from django.views.generic import simple

from blog.models import BlogPost

def home(request):
    blogpost_list = BlogPost.objects.all()
    return simple.direct_to_template(request, 'blog/home.html',
                                     {'blogpost_list': blogpost_list})


def post_detail(request, year, month, day, slug):
    return simple.direct_to_template(request, 'blog/post_detail.html')
