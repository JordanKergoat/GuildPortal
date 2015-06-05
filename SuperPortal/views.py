# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from .models import GuildSettings
# Create your views here.


def index(request):
    context = {}
    context['short_description'] = GuildSettings.objects.all().first().short_guild_description
    return render(request, "SuperPortal/index.html", context=context)