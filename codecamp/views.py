from django.shortcuts import get_object_or_404, render, render_to_response
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from models import FrontpageScroller, Speaker, Session, SessionForm


def speakers_index(request):
    speaker_list = Speaker.objects.all()
    return render_to_response('speakers/index.html', {
                              'PAGE_NAME': 'Speakers',
                              'speaker_list': speaker_list,
                              'request': request})


def speaker_detail(request, slug, id):
    speaker = get_object_or_404(Speaker, pk=id)
    return render_to_response('speakers/detail.html', {
                              'PAGE_NAME': speaker.first_name,
                              'speaker': speaker,
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
            try:
                session.save()
                messages.add_message(request, messages.SUCCESS, 'Thanks! Session saved successfully.')
                return HttpResponseRedirect(reverse('codecamp.views.session_submit'))
            except IntegrityError:
                messages.add_message(request, messages.ERROR, 'There was an error saving your information please email help@southdakotacodecamp.net or contact us on twitter @sdcodecamp')
                return HttpResponseRedirect(reverse('codecamp.views.session_submit'))
    else:
        session = SessionForm()
        print "returning new form"

    return render(request, 'sessions/submit.html', {
                              'request': request,
                              'form': session, })


def scroller(request):
    scrollers = FrontpageScroller.objects.all()
    for scroller in scrollers:
        print dir(scroller)
    return render(request, 'codecamp/scroller.html', {
        "scrollers": scrollers,
        'request': request})
