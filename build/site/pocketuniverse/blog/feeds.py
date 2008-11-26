from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed

from blog.models import BlogPost

class LatestPosts(Feed):
    title = "pocketuniverse.ca blog posts"
    subtitle = "The latests posts to pocketuniverse.ca."
    link = "/"
    author_name = 'Sam Bull'

    title_template = 'blog/_blogpost_title.html'
    description_template = 'blog/_blogpost_body.html'

    feed_type = Atom1Feed

    def items(self):
        return BlogPost.objects.order_by('-pub_date')[:5]

    def item_pubdate(self, item):
        return item.pub_date