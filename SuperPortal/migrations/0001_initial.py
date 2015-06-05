# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('guild_name', models.CharField(max_length=120, verbose_name='Guild name')),
                ('guild_motto', models.CharField(max_length=256, verbose_name='Guild motto')),
                ('guild_chief', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('site', models.OneToOneField(related_name='usersettings', null=True, editable=False, to='sites.Site')),
                ('user', models.ForeignKey(related_name='usersettings', editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Guild Settings',
                'verbose_name_plural': 'Guild Settings',
            },
        ),
    ]
