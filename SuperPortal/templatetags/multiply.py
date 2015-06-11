__author__ = 'Jordan'

from django.template import Library

register = Library()


@register.filter
def multiply(a, b):
    return a * b