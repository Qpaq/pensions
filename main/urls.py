from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<reference>\d+)/$', 'detail', name='detail'),
    url(r'^(?P<reference>\d+)/edit/$', 'edit', name='detail_edit'),
    url(r'^(?P<reference>\d+)/detail$', 'detail_form', name='detail_form'),
    url(r'^(?P<reference>\d+)/edit_form/$', 'edit_form', name='detail_edit_form'),
)
