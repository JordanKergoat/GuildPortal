from braces.views import LoginRequiredMixin
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView
from Forum.models import Forum, Category, Thread, Post


class IndexListCategoryView(LoginRequiredMixin, ListView):
    model = Category


class IndexCategoryView(LoginRequiredMixin, DetailView):
    model = Category
    slug_field = 'slug'
    slug_url_kwarg = 'category'


class DetailForumView(LoginRequiredMixin, DetailView):
    model = Forum
    slug_field = 'slug'
    slug_url_kwarg = 'title'


class CreateThreadView(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ('title',)
    template_name = 'Forum/create_thread.html'

    def get_success_url(self):
        return reverse('thread_detail', kwargs={'category': self.kwargs['category'],
                                                'title': self.kwargs['title'],
                                                'thread_name': Thread.objects.get(id=self.object.id).slug })

    def form_valid(self, form):
        thread = form.save(commit=False)


        thread.creator = self.request.user
        thread.forum = Forum.objects.get(slug=self.kwargs['title'])

        threadtmp = thread.save()
        # self.slug = slugify(self.object.title + str(self.object.id))
        return super(CreateThreadView, self).form_valid(form)


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('body',)
    template_name = 'Forum/create_thread.html'

    def get_success_url(self):
        return reverse('thread_detail', kwargs={'category':self.kwargs['category'], 'title':self.kwargs['title'], 'thread_name':self.kwargs['thread_name']})

    #category=thread.forum.category.slug title=thread.forum.slug thread_name=thread.slug
    def form_valid(self, form):
        post = form.save(commit=False)
        post.creator = self.request.user
        post.title = self.kwargs['thread_name']
        post.thread = Thread.objects.get(forum__category__slug=self.kwargs['category'], slug=self.kwargs['thread_name'])
        post.save()
        return super(CreatePostView, self).form_valid(form)
    # title = models.CharField(max_length=60)
    # slug = models.CharField(max_length=60, blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    # creator = models.ForeignKey(User, blank=True, null=True)
    # thread = models.ForeignKey(Thread, related_name="posts")
    # body = models.TextField(max_length=10000)

class DetailThreadView(LoginRequiredMixin, DetailView):
    model = Thread
    slug_field = 'slug'
    slug_url_kwarg = 'thread_name'


def index(request):
    return HttpResponse('Forum')