import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import first
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from GuildPortal import settings


class Category(models.Model):
    name = models.CharField(_('Category'), max_length=150)
    slug = models.CharField(_('Slug'), max_length=150, db_index=True, blank=True)
    position = models.SmallIntegerField(_('Position'))

    class Meta:
        ordering = ["position"]
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return "%s" % self.name

class Forum(models.Model):
    title = models.CharField(_('Title'), max_length=80)
    slug = models.CharField(_('Slug'), max_length=80, db_index=True, blank=True)
    description = models.CharField(_('Description'), max_length=80, blank=True)
    position = models.SmallIntegerField(_('Position'))
    category = models.ForeignKey(Category, related_name="forums")
    closed = models.BooleanField(_('Closed'), default=False)
    view_count = models.IntegerField(default=0, editable=False)
    post_count = models.IntegerField(default=0, editable=False)

    class Meta:
        ordering = ["position"]
        verbose_name = _('Forum')
        verbose_name_plural = _('Forums')

    def __str__(self):
        return "%s" % self.title

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

    def update_post_count(self):
        post_count = 0
        for thread in self.threads.all():
            thread.update_reply_count()
            post_count += thread.reply_count + 1  # add one for the thread itself
        self.post_count = post_count
        self.save()

class Thread(models.Model):
    title = models.CharField(max_length=60)
    slug = models.CharField(max_length=60, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum = models.ForeignKey(Forum, related_name="threads")
    view_count = models.IntegerField(default=0, editable=False)
    reply_count = models.IntegerField(default=0, editable=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return "%s - %s" % (self.title, self.forum.title)

    def num_posts(self):
        return self.posts.count()

    def num_replies(self):
        return self.num_posts() - 1

    def last_post(self):
        return first(self.posts.all())

    def inc_views(self):
        self.view_count += 1
        self.save()
        self.forum.inc_views()

    def update_reply_count(self):
        self.reply_count = self.posts.all().count()
        self.save()


class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.CharField(max_length=60, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    thread = models.ForeignKey(Thread, related_name="posts")
    body = models.TextField(max_length=10000)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return "%s" % self.title

    def editable(self, user):
        if user == self.creator:
            if timezone.now() < self.created + datetime.timedelta(**settings.FORUMS_EDIT_TIMEOUT):
                return True
        return False



@receiver(pre_save, sender=Forum)
def slugify_forum(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)

@receiver(pre_save, sender=Thread)
def slugify_thread(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title + str(instance.id))

@receiver(pre_save, sender=Post)
def slugify_post(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)

@receiver(pre_save, sender=Category)
def slugify_category(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)