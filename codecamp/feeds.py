from django.utils.feedgenerator import Atom1Feed
from django.contrib.syndication.views import Feed
from models import Session

class SessionsFeed(Feed):
    feed_type = Atom1Feed
    title = "South Dakota Codecamp Sessions"
    link = "/sessions/"
    description = "Contains the list os South Dakota Codecamp Sessions."

    def items(self):
        return Session.objects.order_by('title')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.abstract