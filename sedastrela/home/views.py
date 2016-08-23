from django.shortcuts import render, get_object_or_404

from sedastrela.events.models import Event
from sedastrela.news.models import News
from sedastrela.menu.models import Menu


def home_view(request):
    events = Event.objects.filter(is_active=True)
    news = News.objects.filter(is_active=True)
    menu, _ = Menu.objects.get_or_create(uid='main_menu')

    posts = []
    for event in events:
        pass

    return render(request, 'sedastrela/home/home.html', {
        'posts': posts,
        'menu': menu,
    })

