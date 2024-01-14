from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^create/?$', views.create, name='pastebin-create'),
    re_path(r'^(?P<urlid>.+)/$', views.show, name='pastebin-show'),
    re_path(r'^(?P<urlid>.+)/raw/?$', views.showraw, name='pastebin-showraw'),
    re_path(r'^(?P<urlid>.+)/reply/?$', views.reply, name='pastebin-reply'),
]
