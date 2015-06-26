from django.http import HttpResponse
from .models import Portal, Category, News, CommentNews
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models.enrollment import CharacterAttribute, Game
# Create your views here.

def index(request, portal_name):
    portal = get_object_or_404(Portal, name=portal_name.replace('_', ' '))
    news_list = News.objects.filter(portal=portal).order_by('-published_date')
    return render(request, "SuperPortal/index.html", context={'portal': portal, 'news_list': news_list})


def news_detail(request, portal_name, category, news_name):
    portal = Portal.objects.get(name=portal_name.replace('_', ' '))
    news = News.objects.get(category__name=category.replace('_', ' '), slug=news_name)
    news.view += 1
    news.save()
    raw_comments = CommentNews.objects.filter(news=news, response=None).order_by('published_date')
    comments = {}
    for comment in raw_comments:
        comments[comment] = CommentNews.objects.filter(response=comment).order_by('published_date')

    return render(request, 'Portal/News/index.html', {'news': news, 'comments': comments})
