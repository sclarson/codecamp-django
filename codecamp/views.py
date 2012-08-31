from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from models import FrontpageScroller, Speaker, Session, SessionForm


def speakers_index(request):
    speaker_list = get_list_or_404(Speaker)
    t = loader.get_template('speakers/index.html')
    c = RequestContext(request, {
        'speaker_list': speaker_list,
        'PAGE_NAME': 'Speakers',
        'request': request})
    response = HttpResponse(t.render(c))
    return response


def speaker_detail(request, slug, id):
    speaker = get_object_or_404(Speaker, pk=id)
    t = loader.get_template('speakers/detail.html')
    c = RequestContext(request, {
        'PAGE_NAME': str(speaker.first_name + ' ' + speaker.last_name),
        'speaker': speaker,
        'request': request})
    response = HttpResponse(t.render(c))
    return response


def sessions_index(request):
    session_list = get_list_or_404(Session)
    t = loader.get_template('sessions/index.html')
    c = RequestContext(request, {
        'PAGE_NAME': 'Sessions',
        'session_list': session_list,
        'request': request})
    response = HttpResponse(t.render(c))
    return response


def session_detail(request, slug, id):
    session = get_object_or_404(Session, pk=id)
    t = loader.get_template('sessions/detail.html')
    c = RequestContext(request, {
        'PAGE_NAME': session.title,
        'session': session,
        'request': request})
    response = HttpResponse(t.render(c))
    return response


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
    t = loader.get_template('sessions/submit.html')
    c = RequestContext(request, {
        'PAGE_NAME': 'Session Submission',
        'form': session,
        'request': request})
    response = HttpResponse(t.render(c))
    return response


def scroller(request):
    scrollers = FrontpageScroller.objects.all()
    for scroller in scrollers:
        print dir(scroller)
    return render(request, 'codecamp/scroller.html', {
        "scrollers": scrollers,
        'request': request})
