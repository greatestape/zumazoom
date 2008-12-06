from django.contrib.comments.feeds import LatestCommentFeed
from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed

from blog.models import BlogPost

class LatestPosts(Feed):
    title = "pocketuniverse.ca blog posts"
    subtitle = "The latest posts to pocketuniverse.ca."
    link = "/"
    author_name = 'Sam Bull'

    title_template = 'blog/_blogpost_title.html'
    description_template = 'blog/_blogpost_body.html'

    feed_type = Atom1Feed

    def items(self):
        return BlogPost.objects.order_by('-pub_date')[:5]

    def item_pubdate(self, item):
        return item.pub_date


class LatestCommentsAtomFeed(LatestCommentFeed):
    def subtitle(self):
        return self.description()

    feed_type = Atom1Feed

    def item_author_name(self, item):
        return item.name
