from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, FormView, UpdateView, View, CreateView
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin, StaffuserRequiredMixin, SelectRelatedMixin
from django.views.generic.base import TemplateView
from Forum.models import Post
from Portal.models import Game, Userprofile, CommentNews, CharacterAttribute
from PortalAdmin.forms import UserForm


class AdminIndexView(LoginRequiredMixin, StaffuserRequiredMixin, TemplateView):
    template_name = 'Administration/index.html'


# DEBUT MEMBRES

class AdminMembersView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = User
    template_name = 'Administration/users/user_list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(AdminMembersView, self).dispatch(request, *args, **kwargs)


class AdminUserDetailView(LoginRequiredMixin, StaffuserRequiredMixin, SelectRelatedMixin, DetailView):
    template_name = 'Administration/users/user_detail.html'
    model = User
    select_related = ['userprofile']
    pk_url_kwarg = 'pk'


class AdminUserUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    template_name = 'Administration/users/user_edit_detail.html'
    model = Userprofile
    fields = ['birthday_date', 'gender', 'job_study', 'status', 'country', 'town', 'image_profile']
    template_name_suffix = '_update_form'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse_lazy('admin_user_detail', kwargs={'pk': self.kwargs['pk']})


class LastPostLastComments(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            choices = {}
            choices['posts'] = list(Post.objects.filter(creator__pk=kwargs['pk']).order_by('created').values("body", "pk")[:10])
            choices['comments'] =list( CommentNews.objects.filter(user__pk=kwargs['pk']).order_by('published_date').values('content', 'news__title', 'news_id')[:10])
            return JsonResponse(choices, safe=False)
# FIN MEMBRES

# DEBUT GAME


class AdminGamesView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = Game
    template_name = 'Administration/games/game_list.html'


class AdminGameDetailView(LoginRequiredMixin, StaffuserRequiredMixin, DetailView):
    model = Game
    template_name = 'Administration/games/game_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(AdminGameDetailView, self).get_context_data(**kwargs)
    #     context['user_list'] = User.objects.all()
    #     return context


class AdminGameCreate(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = Game
    template_name = 'Administration/games/game_add.html'
    fields = ['name', 'image', 'url_api']

    def get_success_url(self):
        return reverse_lazy('admin_game_characters_details_add', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        game = form.save()
        self.kwargs['pk'] = game.id
        return super(AdminGameCreate, self).form_valid(form)


class AdminGameUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    template_name = 'Administration/games/game_edit_detail.html'
    model = Game
    fields = []
    pk_url_kwarg = 'pk'

# DEBUT GAME CHARACTERS

class AdminGameCharactersCreate(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = CharacterAttribute
    template_name = 'Administration/games/add_character_attibutes.html'
    fields = ['attribute_name', 'attribute_value']

    def form_valid(self, form):

        form.instance.for_game = Game.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(AdminGameCharactersCreate, self).form_valid(form)

# FIN GAME CHARACTERS

# FIN GAMES