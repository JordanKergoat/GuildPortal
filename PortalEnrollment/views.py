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

from battlenet.oauth2 import BattleNetOAuth2
from django.http import HttpResponseRedirect

# def tmp(request):
#     if request.GET.get('code'):
#         if request.GET.get('state') and request.session.get('state'):
#             if request.GET['state'] == request.session['state']:
#                 bnet = BattleNetOAuth2(key="r5k3eqmj988fh6wsdvu8gh57rzbap62r", redirect_uri="https://127.0.0.1:8000/recrutement/tmp/", secret="HgR8zqCCsPUA75xQHVa4WQktqnnmmyCZ")
#                 data = bnet.retrieve_access_token(request.GET['code'])
#                 print "data", data
#
# def redirect_to_bnet(request):
#     bnet = BattleNetOAuth2(key="r5k3eqmj988fh6wsdvu8gh57rzbap62r", redirect_uri="https://127.0.0.1:8000/recrutement/tmp/", secret="HgR8zqCCsPUA75xQHVa4WQktqnnmmyCZ")
#     url, state = bnet.get_authorization_url()
#     print 'URL' , url
#     print 'STATE', state
#     # save state somewhere for checking the redirect response against
#     request.session['state'] = state
#     return HttpResponseRedirect(url)

def redirect_to_bnet(request):
    return

def tmp(request):
    from battlenet.community.wow.characters import Character
    char = Character(name="Xunis", realm="Ysondre", apikey="r5k3eqmj988fh6wsdvu8gh57rzbap62r", locale="fr")
    return HttpResponse(char.get())
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
    success_url = ""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(OpenEnrollementView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        for x in CharacterAttribute.objects.filter(for_game=Game.objects.filter(id=self.request.POST['game_choice'])).distinct('attribute_name'):
            form.instance.roles.add(CharacterAttribute.objects.filter(attribute_name=x.attribute_name, id=self.request.POST[x.attribute_name.field_value]).first())
        form.instance.open = True
        form.save()
        return super(OpenEnrollementView, self).form_valid(form)


class EnrollementView(FormView):
    template_name = "Portal/Enrollement/enrollment.html"
    form_class = EnrollementForm
    success_url = ""

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(EnrollementView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EnrollementView, self).get_context_data(**kwargs)
        context['enrollment_setting'] = EnrollmentSettings.objects.get(id=self.kwargs['id_application'])
        return context


    def form_valid(self, form):
        enrollment_setting = EnrollmentSettings.objects.get(id=self.kwargs['id_application'])
        form.instance.game_choice = enrollment_setting.game_choice
        form.instance.user = self.request.user
        form.instance.open = True
        form.save()
        for x in enrollment_setting.roles.all():
            form.instance.roles.add(x)
        form.save()
        return super(EnrollementView, self).form_valid(form)



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