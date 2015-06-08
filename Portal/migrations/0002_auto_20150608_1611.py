# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Portal.models.news
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0001_initial'),
        ('SuperPortal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='portal',
            name='portal',
            field=models.ForeignKey(null=True, blank=True, to='SuperPortal.SuperPortal'),
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(verbose_name='Select categories', help_text='News category', to='Portal.Category'),
        ),
        migrations.AddField(
            model_name='news',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='portal',
            field=models.ForeignKey(verbose_name='Which portal to publish on ?', default=1, to='Portal.Portal'),
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(help_text='Tags list', db_constraint=Portal.models.news.Tag, to='Portal.Tag'),
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
            field=models.ForeignKey(default='', to='Portal.Game'),
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
