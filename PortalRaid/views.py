from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView, FormView, ListView, DetailView
from PortalRaid.forms import CharacterForm
from PortalRaid.models import Realm, CharacterModel


class ServerListView(View):
    """
    :return json for ajax request to have list of server for each game in select option
    """
    def get(self, request, *args, **kwargs):
        realms = Realm.objects.filter(game=request.GET['game'])
        realm = [{'id': realm.id, 'name': realm.name} for realm in realms]
        return JsonResponse(realm, safe=False)

class DetailsCharacter(DetailView):
    model = CharacterModel
    context_object_name = 'character'

    def get_context_data(self, **kwargs):
        context = super(DetailsCharacter, self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DetailsCharacter, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        character =  get_object_or_404(self.model, pk=self.kwargs.get('pk', None))
        if character.user == self.request.user:
            return character
        raise PermissionDenied()


class DetailsCharacterFromAPI(View):
    def get(self, request, *args, **kwargs):
        char = CharacterModel.objects.get(pk=self.request.GET['char'])
        if char.user == self.request.user:
            #print self.request.GET['fields']
            from battlenet.community.wow.characters import Character
            tmp = Character(name=char.name, realm=char.server.name, locale='fr',
                            apikey="r5k3eqmj988fh6wsdvu8gh57rzbap62r").get(fields=['appearance'])
            print tmp
            return JsonResponse(tmp[1], safe=False)


class ListCharactersUser(ListView):
    """
    :return List of all characters for each user
    """
    model = CharacterModel

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ListCharactersUser, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset



class NewCharacterFormView(FormView):
    """
    Allow to add new characters on website. User can select game and server on list.
    """
    template_name = 'PortalRaid/new_character.html'
    form_class = CharacterForm
    success_url = reverse_lazy('list_characters_user')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(NewCharacterFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.url = form.instance.game.url_api + 'character/' + form.instance.server.name + '/' + form.instance.name + '/'
        form.save()
        return super(NewCharacterFormView, self).form_valid(form)