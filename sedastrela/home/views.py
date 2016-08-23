from django.shortcuts import render, get_object_or_404

from sedastrela.events.models import Event
from sedastrela.news.models import News


def home_view(request):
    events = Event.objects.filter(is_active=True)
    news = News.objects.filter(is_active=True)

    return render(request, 'sedastrela/home/home.html', {
        'events': events,
        'event_last': events.last(),
        'news': news,
        'news_last3': news[:3],
    })

