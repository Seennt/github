# -*- coding: utf-8 -*-
""" Module: models as part of: todo_list

    Created by: Reinier on 22-10-2017. A model is the single, definitive source of information about your data.
    It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a
    single database table.

    TODO:
        - Nothing for this moment.

"""
from django.db import models
from django.urls import reverse


# Create your models here.
class Action(models.Model):
    """: The class: "Action", is part of module: "models".

    A Action model to represent the database table Action. A action that needs to be done to fulfill a particular
    goal.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

    """
    #: description(CharField): Action description.
    description = models.CharField(max_length=200)

    #: subject(CharField): Action subject.
    subject = models.CharField(max_length=64)

    #: created(DateField): Creation date of action.
    created = models.DateField(auto_now_add=True)

    #: filed(DateField): Date when action is filed.
    filed = models.DateField(null=True)

    #: completed(BooleanField): Action is final.
    completed = models.BooleanField(default=0)


class Detail(models.Model):
    """: The class: "Detail", is part of module: "models".

    A Detail model to represent the database table Detail. details holds the steps that explains how a certain
    action is solved or what its actual status is.

    Note:
        - Do not include the `self` parameter in the ``Args`` section.
        - The __init__ method is documented as a docstring on the __init__ method itself.
        - Class attributes, variables owned by the class itself. All values of class attributes are the same
          for each Instance.

    """
    #: explanation(BooleanField): Step explained to fulfill action.
    explanation = models.CharField(max_length=200, null=True)

    #: edited(DateField): Date action adjusted.
    edited = models.DateField(auto_now_add=True)

    #: action(ForeignKey): Relation to action.
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
