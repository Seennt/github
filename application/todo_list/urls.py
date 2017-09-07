from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.List.as_view(), name='index'),
    url(r'^page/(?P<page>\d+)/$', views.List.as_view(), name='page'),
    url(r'^detail/(?P<pk>\d+)/$', views.Detail.as_view(), name='detail'),
    url(r'^remove/(?P<pk>\d+)/$', views.Remove.as_view(), name='remove'),
    url(r'^create/$', views.Action.as_view(), name='create'),
]
