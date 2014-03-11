from django.conf.urls import patterns, include, url
from main import cbviews

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<reference>\d+)/$', 'detail', name='detail'),
    url(r'^(?P<reference>\d+)/edit/$', 'edit', name='detail_edit'),
    url(r'^(?P<reference>\d+)/detail$', 'detail_form', name='detail_form'),
    url(r'^(?P<reference>\d+)/edit_form/$', 'edit_form', name='detail_edit_form'),


    #url(r"^cbv/create/$",cbviews.PensionerCreateView.as_view(),name="cbv_create"),
    url(r"^cbv/(?P<pk>\d+)/detail/$", cbviews.PensionerDetailView.as_view(),name="cbv_detail",),
    url(r"^cbv/(?P<pk>\d+)/detail_form/$", cbviews.PensionerDetailViewForm.as_view(),name="cbv_detail_form"),
    url(r"^cbv/(?P<pk>\d+)/edit_form/$", cbviews.PensionerUpdateViewForm.as_view(), name="cbv_edit_form"),
    url(r"^cbv/$", cbviews.PensionerListView.as_view(), name="cbv_list"),
)
