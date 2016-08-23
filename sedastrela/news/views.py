from django.shortcuts import render, get_object_or_404

from sedastrela.news.models import News


def news_view(request, id, _):
    news = get_object_or_404(News, id=id)
    return render(request, 'sedastrela/news/news.html', {
        'news': news,
    })

