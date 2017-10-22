""" Module: urls as part of: system

    Created by: Reinier on 22-10-2017. The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/

    Examples:
        Function views
            1. Add an import:  from my_app import views
            2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
        Class-based views
            1. Add an import:  from other_app.views import Home
            2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
        Including another URLconf
            1. Import the include() function: from django.conf.urls import url, include
            2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

    TODO:
        - No topics for now.

"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'', include('application.seennt.urls', namespace='seennt')),
    url(r'^auth/', include('utility.authenticate.urls', namespace='authenticate')),
    url(r'^todo-list/', include('application.todo_list.urls', namespace='todo-list')),
    url(r'^admin/', admin.site.urls),
]
