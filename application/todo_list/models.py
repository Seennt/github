from django.db import models
from django.urls import reverse


# Create your models here.
class Action(models.Model):
    """

    """
    description = models.CharField(max_length=200)
    subject = models.CharField(max_length=64)
    created = models.DateField(auto_now_add=True)
    filed = models.DateField(null=True)
    completed = models.BooleanField(default=0)


class Detail(models.Model):
    """

    """
    explanation = models.CharField(max_length=200, null=True)
    edited = models.DateField(auto_now_add=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
