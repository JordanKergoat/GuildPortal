from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from Forum.models import Forum, Category, Thread


class IndexListCategoryView(ListView):
    model = Category


class IndexCategoryView(DetailView):
    model = Category
    slug_field = 'slug'
    slug_url_kwarg = 'category'

class DetailForumView(DetailView):
    model = Forum
    slug_field = 'slug'
    slug_url_kwarg = 'title'


class DetailThreadView(DetailView):
    model = Thread
    slug_field = 'slug'
    slug_url_kwarg = 'thread_name'

def index(request):
    return HttpResponse('Forum')