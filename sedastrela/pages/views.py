from django.shortcuts import render, get_object_or_404

from sedastrela.pages.models import Page


def page_view(request, id, slug):
    page = get_object_or_404(Page, id=id)
    return render(request, 'sedastrela/pages/page.html', {
        'page': page,
    })

