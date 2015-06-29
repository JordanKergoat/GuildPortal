from django.db import models
from django.template.defaultfilters import first
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(_('Category'), max_length=150)
    slug = models.CharField(_('Slug'), max_length=150, db_index=True, blank=True)
    position = models.SmallIntegerField(_('Position'))

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return "%s" % self.name

class Forum(models.Model):
    title = models.CharField(_('Title'), max_length=80)
    slug = models.CharField(_('Slug'), max_length=80, db_index=True, blank=True)
    description = models.CharField(_('Description'), max_length=80, blank=True)
    position = models.SmallIntegerField(_('Position'))
    category = models.ForeignKey(Category, related_name="forums")
    closed = models.BooleanField(_('Closed'), default=False)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return self.title.decode('ascii', 'ignore')

    def num_posts(self):
        return sum([t.num_posts() for t in self.threads.all()])

    def last_post(self):
        """Go over the list of threads and find the most recent post."""
        threads = self.threads.all()
        last = None
        for thread in threads:
            lastp = thread.last_post()
            if lastp and (not last or lastp.created > last.created):
                last = lastp
        return last

class Thread(models.Model):
    title = models.CharField(max_length=60)
    slug = models.CharField(max_length=60, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum = models.ForeignKey(Forum, related_name="threads")

    class Meta:
        ordering = ["-created"]

    def num_posts(self):
        return self.posts.count()

    def num_replies(self):
        return self.num_posts() - 1

    def last_post(self):
        return first(self.posts.all())


class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.CharField(max_length=60, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    thread = models.ForeignKey(Thread, related_name="posts")
    body = models.TextField(max_length=10000)

    class Meta:
        ordering = ["created"]