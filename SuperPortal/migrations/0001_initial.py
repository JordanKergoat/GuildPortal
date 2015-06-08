# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('guild_name', models.CharField(verbose_name='Guild name', max_length=120)),
                ('guild_motto', models.CharField(verbose_name='Guild motto', max_length=256)),
                ('short_guild_description', models.CharField(verbose_name='Short description about your guild', default='', max_length=120)),
                ('guild_description', models.TextField(verbose_name='Description about your guild', default='')),
                ('tag', models.CharField(verbose_name='Tag', default='', max_length=10)),
                ('group_can_vote', models.ManyToManyField(blank=True, related_name='group_can_vote', to='auth.Group')),
                ('group_can_write_news', models.ManyToManyField(blank=True, related_name='group_can_write_news', to='auth.Group')),
                ('group_can_write_wiki', models.ManyToManyField(blank=True, related_name='group_can_write_wiki', to='auth.Group')),
                ('guild_chief', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Guild Settings',
                'verbose_name_plural': 'Guild Settings',
            },
        ),
        migrations.CreateModel(
            name='SuperPortal',
            fields=[
                ('id_uuid', models.CharField(max_length=36, default='c63cbbe9-d0b5-4c67-ae76-98b842445faa', editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
