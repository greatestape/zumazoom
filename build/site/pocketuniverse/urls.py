from django.conf.urls.defaults import *
from django.contrib import admin

from blog.feeds import LatestPosts

feeds = {
    'latest': LatestPosts,
}

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'blog.views.home'),
    (r'^archive/', include('blog.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),

    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)
