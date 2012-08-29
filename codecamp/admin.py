from django.contrib import admin
from codecamp.models import Session, SubmittedSession, Speaker, FrontpageScroller


class SpeakerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['first_name'] + ['last_name']}


class SessionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(SubmittedSession)
admin.site.register(FrontpageScroller)
