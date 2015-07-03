
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, FormView, UpdateView
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin, StaffuserRequiredMixin, SelectRelatedMixin
from django.views.generic.base import TemplateView
from Portal.models import Game, Userprofile
from PortalAdmin.forms import UserForm

def test_context(template_name):

    def decorator(function):
        def additionnal_context(function):

            def wrapper(**kwargs):
                TemplateView.template_name = template_name
                context = {}
                context['games'] = ['toto', 'titi']
                return context

            return wrapper

        TemplateView.get_context_data = method_decorator(additionnal_context)(TemplateView.get_context_data)
        return TemplateView

    return decorator


@test_context('Administration/index.html')
# class AdminIndexView(LoginRequiredMixin, StaffuserRequiredMixin, TemplateView):
class AdminIndexView(TemplateView):
    pass
    # template_name = 'Administration/index.html'




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