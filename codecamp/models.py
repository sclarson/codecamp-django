from django.db import models
from datetime import date


class Speaker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    twitter = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    website = models.URLField()
    company_website = models.URLField()
    slug = models.SlugField()

    def __unicode__(self):
        return self.first_name + " " + self.last_name


class Session(models.Model):
    YEARS = ((2012, 2012), )
    speakers = models.ManyToManyField(Speaker)
    title = models.CharField(max_length=60)
    abstract = models.TextField()
    year = models.IntegerField(choices=YEARS, default=date.today().year)

    def __unicode__(self):
        return self.title
