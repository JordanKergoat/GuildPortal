# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildSettings',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('guild_name', models.CharField(verbose_name='Guild name', max_length=120)),
                ('guild_motto', models.CharField(verbose_name='Guild motto', max_length=256)),
                ('short_guild_description', models.CharField(verbose_name='Short description about your guild', max_length=120, default='')),
                ('guild_description', models.TextField(verbose_name='Description about your guild', default='')),
                ('tag', models.CharField(verbose_name='Tag', max_length=10, default='')),
                ('guild_chief', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Guild Settings',
                'verbose_name': 'Guild Settings',
            },
        ),
        migrations.CreateModel(
            name='SuperPortal',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
    ]
