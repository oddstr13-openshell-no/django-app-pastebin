from django.conf.urls import patterns, include, url

urlpatterns = patterns('pastebin.views',
    url(r'^$', 'index'),
    url(r'^create/?$', 'create'),
    url(r'^(?P<urlid>.+)/$', 'show'),
    url(r'^(?P<urlid>.+)/raw/?$', 'showraw'),
    url(r'^(?P<urlid>.+)/reply/?$', 'reply'),
)
