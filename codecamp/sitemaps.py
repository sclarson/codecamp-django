from django.contrib.sitemaps import Sitemap
from codecamp.models import Session, Speaker
from datetime import datetime, timedelta



class CodeCampSiteMapBase(Sitemap):
    changefreq = "never"
    priority = 0.5

    # Add last modified to models :(
    def lastmod(self, obj):
        return datetime.now() - timedelta(days=7)


class SessionSiteMap(CodeCampSiteMapBase):
    def items(self):
        return Session.objects.all()


class SpeakerSiteMap(CodeCampSiteMapBase):
    def items(self):
        return Speaker.objects.all()
