 # import the settings file
from django.conf import settings


def required_site_settings(context):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'SITE_NAME': settings.SITE_NAME,
            'MEDIA_URL': settings.MEDIA_URL}

