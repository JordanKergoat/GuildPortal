
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, FormView, UpdateView
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin, StaffuserRequiredMixin, SelectRelatedMixin
from django.views.generic.base import TemplateView
from Portal.models import Game, Userprofile
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
    select_related = ['Userprofile']
    pk_url_kwarg = 'pk'


class AdminUserUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    template_name = 'Administration/users/user_edit_detail.html'
    model = User
    fields = []
    pk_url_kwarg = 'pk'


# FIN MEMBRES

# DEBUT GAME

class AdminGamesView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = Game
    template_name = 'Administration/games/game_list.html'


class AdminGameUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    template_name = 'Administration/users/user_edit_detail.html'
    model = Game
    fields = []
    pk_url_kwarg = 'pk'

# FIN GAMES