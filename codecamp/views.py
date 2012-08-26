from django.shortcuts import get_object_or_404, render, render_to_response
from django.contrib import messages
from models import Speaker, Session, SessionForm


def speakers_index(request):
    speaker_list = Speaker.objects.all()
    return render_to_response('speakers/index.html', {
                              'PAGE_NAME': 'Speakers',
                              'speaker_list': speaker_list,
                              'request': request})


def speaker_detail(request, slug, id):
    speaker = get_object_or_404(Speaker, pk=id)
    photo_url = str(speaker.photo.url)
    return render_to_response('speakers/detail.html', {
                              'PAGE_NAME': speaker.first_name,
                              'speaker': speaker,
                              'photo': photo_url.replace('webroot/', ''),
                              'request': request
                              })


def sessions_index(request):
    session_list = Session.objects.all()
    return render_to_response('sessions/index.html', {
                              'PAGE_NAME': 'Sessions',
                              'session_list': session_list,
                              'request': request})


def session_detail(request, slug, id):
    session = get_object_or_404(Session, pk=id)
    return render_to_response('sessions/detail.html', {
                              'PAGE_NAME': session.title,
                              'session': session,
                              'request': request})


def session_submit(request):
    if request.method == 'POST':
        session = SessionForm(request.POST)
        if session.is_valid():
            session.save()
            messages.add_message(request, messages.SUCCESS, 'Thanks! Session saved successfully.')
            print "saved successfully"
    else:
        session = SessionForm()
        print "returning new form"

    return render(request,'sessions/submit.html', {
                              'request': request,
                              'form': session, })
