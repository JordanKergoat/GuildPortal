from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.
from django.template.loader import render_to_string
from django.views.generic import FormView, View, TemplateView, ListView
from Portal.models import Game, CharacterAttribute
from PortalEnrollment.forms import OpenEnrollementForm, EnrollementForm

#
# def EnrollementView(request):
#     print request.GET
#     context = {
#         'form': EnrollementForm()
#     }
#     return render_to_response('Portal/Enrollement/index.html', context=context)
from PortalEnrollment.models import Enrollement, EnrollmentSettings


class OpenEnrollementView(FormView):
    template_name = "Portal/Enrollement/open_enrollment.html"
    form_class = OpenEnrollementForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        for x in CharacterAttribute.objects.filter(for_game=Game.objects.filter(id=self.request.POST['game_choice'])).distinct('attribute_name'):
            form.instance.roles.add(CharacterAttribute.objects.filter(attribute_name=x.attribute_name, id=self.request.POST[x.attribute_name.field_value]).first())

        form.save()



class EnrollementView(FormView):
    template_name = "Portal/Enrollement/enrollment.html"
    form_class = EnrollementForm

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super(EnrollementView, self).get_initial()
        initial['game_choice'] = EnrollmentSettings.objects.filter(id=self.kwargs['id_application']).first().game_choice
        return initial

    def form_valid(self, form):
        form.instance.game_choice = EnrollmentSettings.objects.filter(id=self.kwargs['id_application']).first().game_choice
        form.instance.user = self.request.user


class EnrollementListView(ListView):
    template_name = 'Portal/Enrollement/enrollement_list.html'
    model = Enrollement


class CharacterAttributesView(TemplateView):
    template_name = 'Portal/Enrollement/characters_attributes.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            game = request.GET['game']
            game = get_object_or_404(Game, name=game)
            choices = {}
            context = self.get_context_data()
            for d in CharacterAttribute.objects.filter(for_game=game).distinct('attribute_name'):
                choices[d.attribute_name] = CharacterAttribute.objects.filter(for_game=game, attribute_name=d.attribute_name)
            context['distinct'] = choices
            return self.render_to_response(context=context)