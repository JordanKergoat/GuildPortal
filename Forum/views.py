from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from Forum.models import Forum, Category


class IndexListCategoryView(ListView):
    model = Category


class IndexCategoryView(DetailView):
    model = Category
    slug_field = 'slug'
    slug_url_kwarg = 'category'


def index(request):
    return HttpResponse('Forum')