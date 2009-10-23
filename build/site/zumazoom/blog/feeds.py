from django.contrib.comments.feeds import LatestCommentFeed
from django.contrib.syndication.feeds import Feed, FeedDoesNotExist
from django.utils.feedgenerator import Atom1Feed

from blog.models import BlogPost, Category

class LatestPosts(Feed):
    title = "zumazoom.com posts"
    subtitle = "The latest posts to zumazoom.com."
    link = "/"
    author_name = 'Dael Stewart'

    title_template = 'blog/_blogpost_title.html'
    description_template = 'blog/_blogpost_body.html'

    feed_type = Atom1Feed

    def items(self):
        return BlogPost.objects.public_posts().order_by('-pub_date')[:5]

    def item_pubdate(self, item):
        return item.pub_date


class LatestPostsInCategory(LatestPosts):
    def get_object(self, bits):
        if len(bits) != 1:
            raise Category.DoesNotExist
        return Category.objects.get(slug__exact=bits[0])

    def title(self, obj):
        return 'zumazoom.com %s posts' % obj.name

    def subtitle(self, obj):
        return 'The latest %s posts to zumazoom.com' % obj.name

    def link(self, obj):
        if not obj:
            raise FeedDoesNotExist
        return obj.get_absolute_url()

    author_name = 'Dael Stewart'

    def items(self, obj):
        return obj.blogpost_set.public_posts().order_by('-pub_date')[:5]


class LatestCommentsAtomFeed(LatestCommentFeed):
    def subtitle(self):
        return self.description()

    feed_type = Atom1Feed

    def item_author_name(self, item):
        return item.name
