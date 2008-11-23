from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^(?P<year>\d{4})/(?P<month>\w+)/(?P<slug>[\w-]+)/$', 'post_detail', name='blog_post_detail'),
)
