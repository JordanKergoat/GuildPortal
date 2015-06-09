# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import Portal.models.news


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SuperPortal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portal',
            name='portal',
            field=models.ForeignKey(blank=True, to='SuperPortal.SuperPortal', null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(verbose_name='Select categories', to='Portal.Category', help_text='News category'),
        ),
        migrations.AddField(
            model_name='news',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='portal',
            field=models.ForeignKey(default=1, verbose_name='Which portal to publish on ?', to='Portal.Portal'),
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(help_text='Tags list', db_constraint=Portal.models.news.Tag, to='Portal.Tag'),
        ),
        migrations.AddField(
            model_name='commentnews',
            name='news',
            field=models.ForeignKey(to='Portal.News'),
        ),
        migrations.AddField(
            model_name='commentnews',
            name='response',
            field=models.ForeignKey(default=1, blank=True, to='Portal.CommentNews', null=True),
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
            field=models.ForeignKey(default=b'', to='Portal.Game'),
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
