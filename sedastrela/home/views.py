from django.shortcuts import render, get_object_or_404

from sedastrela.events.models import Event
from sedastrela.news.models import News


def home_view(request):
    events = Event.objects.filter(is_active=True)
    news = News.objects.filter(is_active=True)

    posts = []
    for event in events:
        pass

    return render(request, 'sedastrela/home/home.html', {
        'posts': posts,
    })

