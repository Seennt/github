# -*- coding: utf-8 -*-
""" Module: admin as part of: collect

    Created by: Reinier on 22-10-2017. Via this admin module maintenance and configuration is made available in
    the Django admin System.

    TODO:
        - Nothing for this moment.
"""
from django.contrib import admin
from utility.collect import models

# Register your models here.


class Url(admin.TabularInline):
    """: The class: "Url", is part of module: "admin".

    Provide a class description here. A good explanation of a class provides a higher readability of the code.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.


    """
    model = models.Url
    extra = 1
    can_delete = True


class Selector(admin.TabularInline):
    """: The class: "Selector", is part of module: "admin".

    A  xpath selector or css selector.

    Raises:
        Explain exceptions that are raised during execution. I.e. ValueError.

    """
    model = models.Selector
    extra = 1
    can_delete = True


class FormData(admin.TabularInline):
    """: The class: "FormData", is part of module: "admin".

    Add form-data form to admin page Configuration.

    Raises:
        All exceptions are handle by the admin class, which we inherit from.

    """
    model = models.FormData
    extra = 1
    can_delete = True


class Cookie(admin.TabularInline):
    """: The class: "Cookie", is part of module: "admin".

    Cookie data, required to fulfill a request

    Raises:
        Explain exceptions that are raised during execution. I.e. ValueError.

    """
    model = models.Cookie
    extra = 1
    can_delete = True


class Meta(admin.TabularInline):
    """: The class: "Meta", is part of module: "admin".

    Meta data, to create a request.

    Raises:
        Explain exceptions that are raised during execution. I.e. ValueError.

    """
    model = models.Meta
    extra = 1
    can_delete = True


class Flag(admin.TabularInline):
    """: The class: "Flag", is part of module: "admin".
    A flag is meant for log purpose.
    Raises:
        Explain exceptions that are raised during execution. I.e. ValueError.

    """
    model = models.Flag
    extra = 1
    can_delete = True


@admin.register(models.Config)
class Robot(admin.ModelAdmin):
    """: The class: "Robot", is part of module: "admin".

    Config a robot.

    """
    inlines = [
        Url,
        Selector,
        FormData,
        Cookie,
        Meta,
        Flag,
    ]


@admin.register(models.Header)
class Header(admin.ModelAdmin):
    """: The class: "Header", is part of module: "admin".

    Config a robot.

    """
    pass
