from django.shortcuts import render
from .forms import EnrollementForm
from .models.enrollment import FieldName, Game
# Create your views here.

def index(request):
    form = EnrollementForm()

    choice_field_name = FieldName.objects.filter(related_to=Game.objects.filter(name="Guild Wars 2"))

    distinct = FieldName.objects.filter(related_to=Game.objects.filter(name="Guild Wars 2")).distinct('field_name')

    choices = {}

    for d in distinct:

        choices[d.field_name] = FieldName.objects.filter(related_to=Game.objects.filter(name="Guild Wars 2"), field_name=d.field_name)



    return render(request, 'index.html', {'form': form, "choice_field_name": choice_field_name, "distinct":choices})