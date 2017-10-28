# -*- coding: utf-8 -*-
""" Module: admin as part of: collect

    Created by: Reinier on 22-10-2017. Via this admin module maintenance and configuration is made available in
    the Django admin System.

    TODO:
        - Nothing for this moment.
        - Integrate Formset URL
        - Integrate Formset Selectors
        - Integrate Formset form-data
        - Integrate Formset meta
        - Integrate Formset cookie
        - Integrate Formset flags
"""
from django.contrib import admin
from utility.collect import models

# Register your models here.


@admin.register(models.Config)
class Robot(admin.ModelAdmin):
    """: The class: "Robot", is part of module: "admin".

    Config a robot.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

    """
    pass


@admin.register(models.Header)
class Robot(admin.ModelAdmin):
    """: The class: "Header", is part of module: "admin".

    Config a robot.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

    """
    pass
