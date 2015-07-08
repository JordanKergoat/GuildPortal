from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, FormView, UpdateView
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin, StaffuserRequiredMixin, SelectRelatedMixin
from django.views.generic.base import View, ContextMixin, TemplateView
from Portal.models import Game, Userprofile, Portal
from django.views.generic import ListView, DetailView, FormView, UpdateView, View, CreateView
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin, StaffuserRequiredMixin, SelectRelatedMixin
from django.views.generic.base import TemplateView
from Forum.models import Post
from Portal.models import Game, Userprofile, CommentNews, CharacterAttribute
from PortalAdmin.forms import UserForm
from PortalRaid.models import Raid, OutRaid
from SuperPortal.models import GuildSettings


class MenuView(object):

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context['games'] = Game.objects.all()
        return context

# def test_context(template_name):
#     def decorator(function):
#         def additionnal_context(function):
#
#             def wrapper(**kwargs):
#                 TemplateView.template_name = template_name
#                 context = {}
#                 context['games'] = ['toto', 'titi']
#                 return context
#
#             return wrapper
#
#         View.get_context_data = method_decorator(additionnal_context)(View.get_context_data)
#         return View
#
#     return decorator


# @test_context('Administration/index.html')
class AdminIndexView(LoginRequiredMixin, StaffuserRequiredMixin, MenuView, TemplateView):
    template_name = 'Administration/index.html'

    def get(self, request, *args, **kwargs):
        try:
            GuildSettings.objects.first()
        except:
            return HttpResponseRedirect(reverse('admin_guild_setting'))


class AdminGuildSetting(LoginRequiredMixin, StaffuserRequiredMixin, MenuView, CreateView):
    template_name = 'Administration/guild_settings.html'
    model = GuildSettings
    feilds = []
# DEBUT MEMBRES

class AdminMembersView(LoginRequiredMixin, StaffuserRequiredMixin, MenuView, ListView):
    model = User
    template_name = 'Administration/users/user_list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(AdminMembersView, self).dispatch(request, *args, **kwargs)


class AdminUserDetailView(LoginRequiredMixin, StaffuserRequiredMixin, SelectRelatedMixin, MenuView, DetailView):
    template_name = 'Administration/users/user_detail.html'
    model = User
    select_related = ['userprofile']
    pk_url_kwarg = 'pk'


class AdminUserUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, MenuView, UpdateView):
    template_name = 'Administration/users/user_edit_detail.html'
    model = Userprofile
    fields = ['birthday_date', 'gender', 'job_study', 'status', 'country', 'town', 'image_profile']
    template_name_suffix = '_update_form'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse_lazy('admin_user_detail', kwargs={'pk': self.object.user.pk})


class LastPostLastComments(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            choices = {}
            choices['posts'] = list(Post.objects.filter(creator__pk=kwargs['pk']).order_by('created').values("body", "pk")[:10])
            choices['comments'] =list( CommentNews.objects.filter(user__pk=kwargs['pk']).order_by('published_date').values('content', 'news__title', 'news_id')[:10])
            return JsonResponse(choices, safe=False)
# FIN MEMBRES

# DEBUT PORTAL
class AdminPortalCreateView(LoginRequiredMixin, SuperuserRequiredMixin, MenuView, CreateView):
    model = Portal
    template_name = 'Administration/games/game_add.html'
    fields = ['portal', 'guild_name', 'active', 'name', 'image']

    def form_valid(self, form):
        form.instance.game = Game.objects.get(pk=self.kwargs['pk_game'])
        form.instance.guild_name = GuildSettings.objects.all().first().guild_name
        form.save()


class AdminPortalUpdate(LoginRequiredMixin, SuperuserRequiredMixin, MenuView, UpdateView):
    model = Portal
    pk_url_kwarg = "pk_game"
    fields = ['portal', 'game', 'active', 'name', 'guild_name', 'image']
    template_name = 'Administration/portals/portal_form.html'

    def get_queryset(self):
        # get_object_or_404(self.model, game_id=self.kwargs['pk_game'])
        query = self.model.objects.filter(game__id=self.kwargs['pk_game'])
        return query
# FIN PORTAL

# DEBUT GAME


class AdminGamesView(LoginRequiredMixin, StaffuserRequiredMixin, MenuView, ListView):
    model = Game
    template_name = 'Administration/games/game_list.html'


class AdminGameDetailView(LoginRequiredMixin, StaffuserRequiredMixin, MenuView, DetailView):
    model = Game
    template_name = 'Administration/games/game_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AdminGameDetailView, self).get_context_data(**kwargs)
        return context

class AdminGameCreate(LoginRequiredMixin, SuperuserRequiredMixin, MenuView, CreateView):
    model = Game
    template_name = 'Administration/games/game_add.html'
    fields = ['name', 'image', 'url_api']

    def get_success_url(self):
        return reverse_lazy('admin_portal_add', kwargs={'pk_game': self.kwargs['pk']})

    def form_valid(self, form):
        game = form.save()
        self.kwargs['pk'] = game.id
        return super(AdminGameCreate, self).form_valid(form)


class AdminGameUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, MenuView, UpdateView):
    template_name = 'Administration/games/game_edit_detail.html'
    model = Game
    pk_url_kwarg = 'pk'
    fields = ['name', 'image', 'url_api']
    template_name_suffix = '_update_form'

# DEBUT GAME CHARACTERS

class AdminGameCharactersCreate(LoginRequiredMixin, SuperuserRequiredMixin, MenuView, CreateView):
    model = CharacterAttribute
    template_name = 'Administration/games/add_character_attibutes.html'
    fields = ['attribute_name', 'attribute_value']

    def form_valid(self, form):

        form.instance.for_game = Game.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(AdminGameCharactersCreate, self).form_valid(form)

# FIN GAME CHARACTERS

# FIN GAMES