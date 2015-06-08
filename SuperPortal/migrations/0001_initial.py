# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guild_name', models.CharField(max_length=120, verbose_name='Guild name')),
                ('guild_motto', models.CharField(max_length=256, verbose_name='Guild motto')),
                ('short_guild_description', models.CharField(default=b'', max_length=120, verbose_name='Short description about your guild')),
                ('guild_description', models.TextField(default=b'', verbose_name='Description about your guild')),
                ('tag', models.CharField(default=b'', max_length=10, verbose_name='Tag')),
                ('group_can_vote', models.ForeignKey(default=1, to='auth.Group')),
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
                ('id', models.CharField(default=b'2cf11621-7496-492a-bb0b-b9a5c1e776cd', max_length=36, serialize=False, editable=False, primary_key=True)),
            ],
        ),
    ]
