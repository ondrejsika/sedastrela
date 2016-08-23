from django.conf.urls import include, url

from sedastrela.news import views

urlpatterns = [
    url(r'^(?P<id>\d+)/(?P<slug>\d+)/$', views.news_view, name='news'),
]

