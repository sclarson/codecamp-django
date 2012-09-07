from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from django.contrib.syndication.views import Feed
from models import Session

class SessionsFeedAtom(Feed):
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

class SessionsFeedRSS2(Feed):
    feed_type = Rss201rev2Feed
    title = "South Dakota Codecamp Sessions"
    link = "/sessions/"
    description = "Contains the list os South Dakota Codecamp Sessions."

    def items(self):
        return Session.objects.order_by('title')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.abstract