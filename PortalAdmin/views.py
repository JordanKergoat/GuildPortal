
from django.shortcuts import render
from django.views.generic.base import TemplateView


class AdminIndexView(TemplateView):
    template_name = 'Administration/index.html'