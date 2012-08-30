from haystack.indexes import *
from haystack import site
from models import Speaker


class SpeakerIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    last_name = CharField()

site.register(Speaker, SpeakerIndex)
