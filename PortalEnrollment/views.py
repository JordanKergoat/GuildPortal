from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from PortalEnrollment.forms import EnrollementForm


class EnrollementView(FormView):
    template_name = "Portal/Enrollement/index.html"
    form_class = EnrollementForm

    def form_valid(self, form):
        pass