# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from .models import GuildSettings
from Portal.models import News
# Create your views here.


def index(request):
    context = {}
    context['short_description'] = GuildSettings.objects.all().first().short_guild_description
    # context['list_portal'] = Portal.objects.all()
    context['news_list'] = News.objects.all().order_by('-published_date')
    return render(request, "SuperPortal/index.html", context=context)