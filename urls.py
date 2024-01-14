from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create/?$', views.create, name='pastebin-create'),
    url(r'^(?P<urlid>.+)/$', views.show, name='pastebin-show'),
    url(r'^(?P<urlid>.+)/raw/?$', views.showraw, name='pastebin-showraw'),
    url(r'^(?P<urlid>.+)/reply/?$', views.reply, name='pastebin-reply'),
]
