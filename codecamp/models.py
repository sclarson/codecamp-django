from django.db import models
from datetime import date


class Speaker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    twitter = models.CharField(blank=True, max_length=40)
    email = models.EmailField(max_length=254)
    website = models.URLField(blank=True)
    company_website = models.URLField(blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-last_name']

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return "/speakers/" % self.slug % ',' % self.id


class Session(models.Model):
    YEARS = ((2012, 2012), )
    speakers = models.ManyToManyField(Speaker)
    title = models.CharField(max_length=60)
    abstract = models.TextField(blank=True, help_text="A short summary of the session.")
    year = models.IntegerField(choices=YEARS, default=date.today().year)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-title']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/sessions/" % self.slug % ',' % self.id
