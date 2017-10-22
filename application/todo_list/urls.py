""" Module: urls as part of: todo_list

    Created by: Reinier on 22-10-2017. URL namespaces allow you to uniquely reverse named URL patterns even if
    different applications use the same URL names.

    Examples:
        Class-based views
            1. Add an import:  from other_app.views import Home
            2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
    TODO:
        - No topics for now.

"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.List.as_view(), name='index'),
    url(r'^page/(?P<page>\d+)/$', views.List.as_view(), name='page'),
    url(r'^detail/(?P<pk>\d+)/$', views.Detail.as_view(), name='detail'),
    url(r'^remove/(?P<pk>\d+)/$', views.Remove.as_view(), name='remove'),
    url(r'^create/$', views.Action.as_view(), name='create'),
]
