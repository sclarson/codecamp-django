from haystack.indexes import *
from haystack import site
from models import Speaker, Session


class SpeakerIndex(SearchIndex):
    """docstring for SpeakerIndex"""
    text = CharField(document=True, use_template=True)
    last_name = CharField(model_attr='last_name')
    first_name = CharField(model_attr='first_name')
    bio = CharField(model_attr='bio')
    company = CharField(model_attr='company')


class SessionIndex(SearchIndex):
    """docstring for SessionIndex"""
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    abstract = CharField(model_attr='abstract')

site.register(Speaker, SpeakerIndex)
site.register(Session, SessionIndex)
