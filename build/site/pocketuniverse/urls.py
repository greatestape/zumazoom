from django.conf.urls.defaults import *
from django.contrib import admin

from blog.feeds import LatestPosts, LatestPostsInCategory, LatestCommentsAtomFeed

feeds = {
    'latest': LatestPosts,
    'categories': LatestPostsInCategory,
    'comments': LatestCommentsAtomFeed,
}

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'blog.views.home'),
    (r'^archive/', include('blog.urls')),

    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),

    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}, name='feeds'),

    (r'^(?P<category_slug>[-\w]+)/$', 'blog.views.category_detail', {},
        'blog_category_detail'),

)
