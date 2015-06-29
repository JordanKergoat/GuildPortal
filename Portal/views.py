from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic.detail import SingleObjectMixin
from PortalEnrollment.forms import CommentEnrollmentForm, CommentNewsForm
from .models import Portal, Category, News, CommentNews
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, FormView, View
from .models.enrollment import CharacterAttribute, Game
# Create your views here.

def index(request, portal_name):
    portal = get_object_or_404(Portal, name=portal_name.replace('_', ' '))
    news_list = News.objects.filter(portal=portal).order_by('-published_date')
    return render(request, "SuperPortal/index.html", context={'portal': portal, 'news_list': news_list})


def news_detail(request, portal_name, category, news_name):
    portal = Portal.objects.get(slug=portal_name)
    news = News.objects.get(category__name=category.replace('_', ' '), slug=news_name)
    news.view += 1
    news.save()
    raw_comments = CommentNews.objects.filter(news=news, response=None).order_by('published_date')
    comments = {}
    for comment in raw_comments:
        comments[comment] = CommentNews.objects.filter(response=comment).order_by('published_date')
    return render(request, 'Portal/News/index.html', {'news': news, 'comments': comments})


class NewsDetailView(DetailView):
    template_name = 'Portal/News/index.html'
    model = News
    context_object_name = 'news'
    slug_field = 'slug'
    slug_url_kwarg = 'news_name'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        query = queryset.get(portal=Portal.objects.get(slug=self.kwargs['portal_name']), category=Category.objects.get(name=self.kwargs['category']),
                                       slug=self.kwargs['news_name'])
        return query

    def get_success_url(self, **kwargs):
            return reverse('news_detail', kwargs={'portal_name': self.kwargs['portal_name'],
                                              'category': self.kwargs['category'],
                                              'news_name': self.kwargs['news_name']})

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentEnrollmentForm()
        comments = {}
        raw_comments = CommentNews.objects.filter(news=self.get_queryset(), response=None).order_by('published_date')
        for comment in raw_comments:
            comments[comment] = CommentNews.objects.filter(response=comment).order_by('published_date')
        context['comments'] = comments
        context['form'] = CommentEnrollmentForm()
        return context

# class EnrollmentDetailView(DetailView):
#     template_name = 'Portal/Enrollement/enrollement_detail.html'
#     model = Enrollement
#     context_object_name = 'enrollment'
#
#     def get_context_data(self, **kwargs):
#         context = super(EnrollmentDetailView, self).get_context_data(**kwargs)
#         context['form'] = CommentEnrollmentForm()
#         return context
#
#     @method_decorator(login_required)
#     @method_decorator(user_passes_test(can_see))
#     def dispatch(self, request, *args, **kwargs):
#         return super(EnrollmentDetailView, self).dispatch(request, *args, **kwargs)
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(self.model, pk=self.kwargs.get('pk', None))
#
#
class CommentNewsFormView(SingleObjectMixin, FormView):
    form_class = CommentNewsForm
    template_name = 'Portal/News/index.html'
    model = News
    slug_field = 'slug'
    slug_url_kwarg = 'news_name'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super(CommentNewsFormView, self).post(request, *args, **kwargs)

    def get_success_url(self, **kwargs):
        return reverse('news_detail', kwargs={'portal_name': self.kwargs['portal_name'],
                                              'category': self.kwargs['category'],
                                              'news_name': self.kwargs['news_name']})

    def form_valid(self, form):
        form.instance.news = self.object
        form.instance.user = self.request.user
        form.instance.response = None
        form.save()
        return super(CommentNewsFormView, self).form_valid(form)


class NewsDetail(View):

    def get(self, request, *args, **kwargs):
        view = NewsDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentNewsFormView.as_view()
        return view(request, *args, **kwargs)
