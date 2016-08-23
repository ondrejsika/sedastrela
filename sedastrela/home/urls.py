from django.conf.urls import include, url

from sedastrela.home import views

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
]

