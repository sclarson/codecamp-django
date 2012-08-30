from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify
from django import forms
from datetime import date
from markdown import markdown


class Speaker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=False,
                           help_text="A short bio of the speaker.")
    company = models.CharField(max_length=100)
    twitter = models.CharField(blank=True, max_length=40)
    email = models.EmailField(blank=False, max_length=254)
    website = models.URLField(blank=True)
    company_website = models.URLField(blank=True)
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to='media/images/speakers')

    class Meta:
        ordering = ['last_name']

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return ('speaker_detail', (), {'slug': self.slug,
                                       'id': self.id})
    get_absolute_url = models.permalink(get_absolute_url)


class Session(models.Model):
    YEARS = ((2012, 2012), )
    speakers = models.ManyToManyField(Speaker)
    title = models.CharField(max_length=60)
    abstract = models.TextField(blank=True,
                                help_text="A short summary of the session.")
    year = models.IntegerField(choices=YEARS, default=date.today().year)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('session_detail', (), {'slug': self.slug,
                                       'id': self.id})
    get_absolute_url = models.permalink(get_absolute_url)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        return super(Session, self).save(*args, **kwargs)


class SubmittedSession(models.Model):
    LEVELS = ((0, "N/A"), (100, 100), (200, 200), (300, 300), (400, 400))
    title = models.CharField(max_length=120)
    level = models.IntegerField(choices=LEVELS, default=0)
    abstract = models.TextField(blank=True,
                                help_text="A short summary of the session.")
    email = models.EmailField(max_length=254)

    def __unicode__(self):
        return "{0} - {1}".format(self.email, self.title)


class SessionForm(ModelForm):
    class Meta:
        model = SubmittedSession


class FrontpageScroller(models.Model):
    body = models.TextField(blank=False, help_text='A short bit of copy to put on the scroller')
    link = models.URLField(blank=False, help_text="The url the button will point at")
    title = models.CharField(max_length=60)

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        return super(FrontpageScroller, self).save(force_insert, force_update)
