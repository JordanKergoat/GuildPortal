from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from Forum.models import Forum, Category


class IndexListCategoryView(ListView):
    model = Category


def index(request):
    return HttpResponse('Forum')