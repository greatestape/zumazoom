from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^(?P<year>\d{4})/(?P<month>\w+)/(?P<day>\d\d?)/(?P<slug>[\w-]+)/$', 'post_detail', name='blog_post_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\w+)/$', 'archive_month', name='blog_archive_month'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<year>\d{4})/(?P<month>\w+)/$', 'archive_month', name='category_archive_month'),
)
