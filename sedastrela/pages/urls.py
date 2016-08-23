from django.conf.urls import include, url

from sedastrela.pages import views

urlpatterns = [
    url(r'^(?P<id>\d+)/(?P<slug>\d+)/$', views.page_view, name='page'),
]

