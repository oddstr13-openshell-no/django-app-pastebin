from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create/?$', views.create),
    url(r'^(?P<urlid>.+)/$', views.show),
    url(r'^(?P<urlid>.+)/raw/?$', views.showraw),
    url(r'^(?P<urlid>.+)/reply/?$', views.reply),
]
