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
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="organize/index.html"), name='index'),
]
