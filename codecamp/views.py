from django.shortcuts import render_to_response
from models import Speaker, Session


def speakers_index(request):
    speaker_list = Speaker.objects.all()
    return render_to_response('speakers/index.html', {
                              'speaker_list': speaker_list,
                              'request': request})

def speaker_detail(request, slug, id):
    speaker = Speaker.objects.get(pk=id)
    return render_to_response('speakers/detail.html', {
                              'speaker': speaker,
                              'request': request
        })


def sessions_index(request):
    session_list = Session.objects.all()
    return render_to_response('sessions/index.html', {
                              'session_list': session_list,
                              'request': request})

def session_detail(request, slug, id):
    session = Session.objects.get(pk=id)
    return render_to_response('sessions/detail.html', {
                              'session': session,
                              'request': request})