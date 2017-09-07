from django import template

register = template.Library()


@register.filter(name='model_name')
def model_name(value):
    return value.__class__.__name__
