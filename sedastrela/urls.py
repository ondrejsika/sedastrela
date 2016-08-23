from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^event/', include('sedastrela.events.urls', namespace='events')),
    url(r'^news/', include('sedastrela.news.urls', namespace='news')),
    url(r'^page/', include('sedastrela.pages.urls', namespace='pages')),
    url(r'^', include('sedastrela.home.urls', namespace='home')),
]

