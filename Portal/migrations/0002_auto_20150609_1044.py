# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Portal.models.news
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('SuperPortal', '0001_initial'),
        ('Portal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='portal',
            name='portal',
            field=models.ForeignKey(to='SuperPortal.SuperPortal', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(to='Portal.Category', help_text='News category', verbose_name='Select categories'),
        ),
        migrations.AddField(
            model_name='news',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='portal',
            field=models.ForeignKey(to='Portal.Portal', default=1, verbose_name='Which portal to publish on ?'),
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(help_text='Tags list', to='Portal.Tag', db_constraint=Portal.models.news.Tag),
        ),
        migrations.AddField(
            model_name='commentnews',
            name='news',
            field=models.ForeignKey(to='Portal.News'),
        ),
        migrations.AddField(
            model_name='commentnews',
            name='response',
            field=models.ForeignKey(to='Portal.CommentNews', default=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='commentnews',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='class',
            name='game',
            field=models.ForeignKey(to='Portal.Game'),
        ),
        migrations.AddField(
            model_name='characterattribute',
            name='attribute_value',
            field=models.ForeignKey(to='Portal.FieldValue'),
        ),
        migrations.AddField(
            model_name='characterattribute',
            name='for_game',
            field=models.ForeignKey(to='Portal.Game'),
        ),
        migrations.AddField(
            model_name='character',
            name='game',
            field=models.ForeignKey(to='Portal.Game', default=''),
        ),
        migrations.AddField(
            model_name='character',
            name='roles',
            field=models.ManyToManyField(to='Portal.CharacterAttribute'),
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='absence',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
