from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^(?P<year>\d{4})/(?P<month>\w+)/(?P<day>\d\d?)/(?P<slug>[\w-]+)/$', 'post_detail', name='blog_post_detail'),
)
