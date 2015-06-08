from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EnrollementForm
from .models.enrollment import CharacterAttribute, Game
# Create your views here.

def index(request, portal_name):
    return HttpResponse('Portail ' + portal_name)
    # form = EnrollementForm()
    #
    # choice_field_name = CharacterAttribute.objects.filter(for_game=Game.objects.filter(name="Guild Wars 2"))
    #
    # distinct = CharacterAttribute.objects.filter(for_game=Game.objects.filter(name="Guild Wars 2")).distinct('attribute_name')
    #
    # choices = {}
    #
    # for d in distinct:
    #     choices[d.attribute_name] = CharacterAttribute.objects.filter(for_game=Game.objects.filter(name="Guild Wars 2"), attribute_name=d.attribute_name)
    # return render(request, 'index.html', {'form': form, "choice_field_name": choice_field_name, "distinct":choices})


# class Index(TemplateView):
#     template_name = 'index.html'
#
#     def get(self, request, *args, **kwargs):



def news_detail(request, portal_name, category, news_name):
    return