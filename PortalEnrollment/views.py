from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, View, TemplateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from Portal.models import Game, CharacterAttribute
from PortalEnrollment.forms import OpenEnrollementForm, EnrollementForm, CommentEnrollmentForm
from PortalEnrollment.models import Enrollement, EnrollmentSettings, EnrollmentVote
from django.contrib.auth.decorators import login_required, user_passes_test



from SuperPortal.models import GuildSettings

#decorator
def can_see(user):
    for group in GuildSettings.objects.all().first().group_can_vote.all():
        if group in user.groups.all():
            return True
    return False

@csrf_exempt
def voteUp(request, pk):
    if can_see(request.user):
        enrollment = Enrollement.objects.get(pk=pk)
        for enrollment_vote in enrollment.enrollmentvote_set.all():
            if enrollment_vote.user == request.user:
                enrollment_vote.vote = True
                enrollment_vote.save()
                serialize = render_to_string('Portal/Enrollement/list_vote.html', {'enrollment': enrollment})
                return JsonResponse({'voteup': enrollment.get_vote_up(), 'votedown': enrollment.get_vote_down(), 'list_vote': serialize })
        vote = EnrollmentVote()
        vote.enrollment = enrollment
        vote.user = request.user
        vote.vote = True
        serialize = render_to_string('Portal/Enrollement/list_vote.html', {'enrollment': enrollment})
        return JsonResponse({'voteup': enrollment.get_vote_up(), 'votedown': enrollment.get_vote_down(), 'list_vote': serialize })
    return HttpResponseForbidden()


@csrf_exempt
def voteDown(request, pk):
    if can_see(request.user):
        enrollment = Enrollement.objects.get(pk=pk)
        for enrollment_vote in enrollment.enrollmentvote_set.all():
            if enrollment_vote.user == request.user:
                enrollment_vote.vote = False
                enrollment_vote.save()
                serialize = render_to_string('Portal/Enrollement/list_vote.html', {'enrollment': enrollment})
                return JsonResponse({'voteup': enrollment.get_vote_up(), 'votedown': enrollment.get_vote_down(),
                                     'list_vote': serialize})
        vote = EnrollmentVote()
        vote.enrollment = enrollment
        vote.user = request.user
        vote.vote = False
        vote.save()
        serialize = render_to_string('Portal/Enrollement/list_vote.html', {'enrollment': enrollment})
        return JsonResponse(
            {'voteup': enrollment.get_vote_up(), 'votedown': enrollment.get_vote_down(), 'list_vote': serialize})
    return HttpResponseForbidden()

class OpenEnrollementView(FormView):
    template_name = "Portal/Enrollement/open_enrollment.html"
    form_class = OpenEnrollementForm

    def form_valid(self, form):
        print(form)
        form.instance.user = self.request.user
        form.save()
        for x in CharacterAttribute.objects.filter(for_game=Game.objects.filter(id=self.request.POST['game_choice'])).distinct('attribute_name'):
            form.instance.roles.add(CharacterAttribute.objects.filter(attribute_name=x.attribute_name, id=self.request.POST[x.attribute_name.field_value]).first())
        form.instance.open = True
        form.save()


class EnrollementView(FormView):
    template_name = "Portal/Enrollement/enrollment.html"
    form_class = EnrollementForm

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super(EnrollementView, self).get_initial()
        initial['game_choice'] = EnrollmentSettings.objects.filter(id=self.kwargs['id_application']).first().game_choice
        return initial

    def form_valid(self, form):
        form.instance.game_choice = EnrollmentSettings.objects.filter(id=self.kwargs['id_application']).first().game_choice
        form.instance.user = self.request.user


class EnrollementListView(ListView):
    template_name = 'Portal/Enrollement/enrollement_list.html'
    model = Enrollement

    @method_decorator(login_required)
    @method_decorator(user_passes_test(can_see))
    def dispatch(self, request, *args, **kwargs):
        return super(EnrollementListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(EnrollementListView, self).get_queryset()
        return qs.filter(open=True)


class EnrollmentDetailView(DetailView):
    template_name = 'Portal/Enrollement/enrollement_detail.html'
    model = Enrollement
    context_object_name = 'enrollment'

    def get_context_data(self, **kwargs):
        context = super(EnrollmentDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentEnrollmentForm()
        return context

    @method_decorator(login_required)
    @method_decorator(user_passes_test(can_see))
    def dispatch(self, request, *args, **kwargs):
        return super(EnrollmentDetailView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs.get('pk', None))


class CommentEnrollmentFormView(SingleObjectMixin, FormView):
    form_class = CommentEnrollmentForm
    template_name = 'Portal/Enrollement/enrollement_detail.html'
    model = Enrollement


    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super(CommentEnrollmentFormView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('enrollment_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.enrollment = self.object
        form.instance.user = self.request.user
        form.instance.response = None
        form.save()
        return super(CommentEnrollmentFormView, self).form_valid(form)


class EnrollmentDetail(View):

    def get(self, request, *args, **kwargs):
        view = EnrollmentDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentEnrollmentFormView.as_view()
        return view(request, *args, **kwargs)


class CharacterAttributesView(TemplateView):
    template_name = 'Portal/Enrollement/characters_attributes.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            game = request.GET['game']
            game = get_object_or_404(Game, name=game)
            choices = {}
            context = self.get_context_data()
            for d in CharacterAttribute.objects.filter(for_game=game).distinct('attribute_name'):
                choices[d.attribute_name] = CharacterAttribute.objects.filter(for_game=game, attribute_name=d.attribute_name)
            context['distinct'] = choices
            return self.render_to_response(context=context)