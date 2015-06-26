# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView

from .models import GuildSettings
from Portal.models import News, Userprofile
from PortalEnrollment.models import EnrollmentSettings
# Create your views here.


def index(request):
    context = {}
    context['short_description'] = GuildSettings.objects.all().first().short_guild_description
    # context['list_portal'] = Portal.objects.all()
    context['news_list'] = News.objects.all().order_by('-published_date')
    context['enrollments'] = EnrollmentSettings.openned_enrollement.all()

    return render(request, "SuperPortal/index.html", context=context)


class Profile(TemplateView):
    template_name = 'SuperPortal/profile/index.html'

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class Members(ListView):
    model = Userprofile
    template_name = 'SuperPortal/members.html'