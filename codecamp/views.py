from django.shortcuts import get_object_or_404, render_to_response
from models import Speaker, Session


def speakers_index(request):
    speaker_list = Speaker.objects.all()
    return render_to_response('speakers/index.html', {
                              'speaker_list': speaker_list,
                              'request': request})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render_to_response('speakers/detail.html', {
                              'speaker': speaker,
                              'request': request
        })


def sessions_index(request):
    session_list = Session.objects.all()
    return render_to_response('sessions/index.html', {
                              'session_list': session_list,
                              'request': request})


def session_detail(request, slug):
    session = get_object_or_404(Session, slug=slug)
    return render_to_response('sessions/detail.html', {
                              'session': session,
                              'request': request})
