import unicodedata
import re
from django.db.models.signals import pre_save
from django.dispatch import receiver

__author__ = 'Alexandre Cloquet'

import datetime
import arrow
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse, reverse_lazy

from .portal_guild import Portal


class Tag(models.Model):
    name = models.CharField(_('Tag'), max_length=64)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return u"%s" % self.name


    def get_news(self):
        return self.news_set.all()

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return u"%s" % self.name

class NewsFeed(models.Model):
    url = models.URLField()

class News(models.Model):
    #TODO Faire en version API -> AngularJs et Mobile
    portal = models.ForeignKey(Portal, verbose_name=_('Which portal to publish on ?'), default=1)
    creator = models.ForeignKey(User)
    category = models.ForeignKey(Category, help_text=_('News category'), verbose_name=_('Select categories'))
    tags = models.ManyToManyField(_('Tag'), Tag, help_text=_('Tags list'))
    published = models.BooleanField(_("Published"), default=False)
    published_date = models.DateTimeField(_('Published date'), auto_now_add=True)
    modification_date = models.DateTimeField(_('Modification date'), blank=True, null=True)
    title = models.CharField(_('Title'), max_length=100, db_index=True)
    slug = models.CharField(_('Slug'), max_length=100, db_index=True, default="")
    content = models.TextField(_('Body'))
    view = models.IntegerField(default=0)
    news_image = models.ImageField(_('News image'), upload_to='news/')

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ['modification_date']

    def __str__(self):
        return u"%s [%s] | %s" % (self.title, self.portal.name, self.content[0:50])

    def get_absolute_url(self):
        print 'portal_name = ', self.portal.name.replace(' ', '_')
        print 'categorie = ', self.category.name.replace(' ', '_')
        print 'title = ', self.title.replace(' ', '_')

        return reverse('Portal.views.news_detail', args=[self.portal.name.replace(' ', '_'), self.category.name.replace(' ', '_'),
                                                           self.slug])
    def get_date_formated(self):
        date = arrow.get(self.published_date)
        date = date.humanize(locale='fr')
        return date


    def get_related(self):
        list_related = []
        for tag in  self.tags.all():
            for news in tag.get_news():
                list_related.append(news)
        return list_related


class Comment(models.Model):
    user = models.ForeignKey(User)
    published_date = models.DateTimeField(_('Published date'), auto_now_add=True)
    content = models.TextField(_('Your comment'), default="")
    response = models.ForeignKey('self', default=1, blank=True, null=True)

    def __str__(self):
        return self.content[0:25]

    def get_date_formated(self):
        date = arrow.get(self.published_date)
        date = date.humanize(locale='fr')
        return date

    class Meta:
        abstract = True


class CommentNews(Comment):
    news = models.ForeignKey(News)

from django.template.defaultfilters import slugify

@receiver(pre_save, sender=News)
def my_callback(sender, instance, *args, **kwargs):
    print 'je clean title'
    instance.slug = slugify(instance.title)
    print instance.slug

# def slugify(str):
#     slug = unicodedata.normalize("NFKD",unicode(str)).encode("ascii", "ignore")
#     slug = re.sub(r"[^\w]+", " ", slug)
#     slug = "-".join(slug.lower().strip().split())
#     return slug