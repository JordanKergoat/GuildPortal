from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.views.generic import ListView
from Forum.models import Category, Forum

__author__ = 'Alexandre Cloquet'


class ListCategoryView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = Category
    template_name = 'Administration/forum/categories_list.html'

class ListForumView(LoginRequiredMixin, StaffuserRequiredMixin, ListView):
    model = Forum
    template_name = 'Administration/forum/forum_list.html'
    ordering = ('category__name')