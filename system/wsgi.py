# -*- coding: utf-8 -*-
""" Module: wsgi as part of: system

    Created by: Reinier on 22-10-2017. When the WSGI server loads your application, Django needs to import the
    settings module — that’s where your entire application is defined. For more information on this file,
    see https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/

    WSGI is the Web Server Gateway Interface. It is a specification that describes how a web server communicates with
    web applications, and how web applications can be chained together to process one request. WSGI is a Python standard
    described in detail in PEP 3333.

    Examples:
        Should be defined in a later state.

    TODO:
        - Provide a intuitive explanation.

"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "system.settings")

application = get_wsgi_application()
