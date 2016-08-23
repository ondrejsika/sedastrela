from django.shortcuts import render, get_object_or_404

from sedastrela.events.models import Event


def event_view(request, id, _):
    event = get_object_or_404(Event, id=id)
    return render(request, 'sedastrela/events/event.html', {
        'event': event,
    })

