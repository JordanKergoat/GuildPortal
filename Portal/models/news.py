__author__ = 'Alexandre Cloquet'

from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.db import models


from .portal_guild import Portal

class Tag(models.Model):
    name = models.CharField(_('Tag'), max_length=64)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return u"%s" % self.name

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
    portal = models.ForeignKey(Portal, verbose_name=_('Which portal to publish on ?'), default=1)
    creator = models.ForeignKey(User)
    category = models.ForeignKey(Category, help_text=_('News category'), verbose_name=_('Select categories'))
    tags = models.ManyToManyField(_('Tag'), Tag, help_text=_('Tags list'))
    published = models.BooleanField(_("Published"), default=False)
    published_date = models.DateTimeField(_('Published date'), auto_now_add=True)
    modification_date = models.DateTimeField(_('Modification date'), blank=True, null=True)
    title = models.CharField(_('Title'), max_length=100, primary_key=True)
    content = models.TextField(_('Body'))
    news_image = models.ImageField(_('News image'), upload_to='news/')

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return u"%s [%s] | %s" % (self.title, self.portal.name, self.content[0:50])
