from django.conf.urls import include, url

from sedastrela.events import views

urlpatterns = [
    url(r'^(?P<id>\d+)/(?P<slug>\d+)/$', views.event_view, name='event'),
]

