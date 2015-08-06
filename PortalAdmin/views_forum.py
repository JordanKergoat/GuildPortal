from django.views.generic import ListView
from Forum.models import Category, Forum

__author__ = 'Alexandre Cloquet'


class ListCategoryView(ListView):
    model = Category
    template_name = 'Administration/forum/categories_list.html'

class ListForumView(ListView):
    model = Forum
    template_name = 'Administration/forum/forum_list.html'