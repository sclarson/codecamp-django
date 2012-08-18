from django.shortcuts import render_to_response
from speakers.models import Speaker


def entries_index(request):
    return render_to_response('speakers/entry_index.html',
                                'speaker_list': Speaker.objects.all())
