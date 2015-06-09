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
<<<<<<< HEAD
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('guild_name', models.CharField(max_length=120, verbose_name='Guild name')),
                ('guild_motto', models.CharField(max_length=256, verbose_name='Guild motto')),
                ('short_guild_description', models.CharField(max_length=120, default='', verbose_name='Short description about your guild')),
                ('guild_description', models.TextField(default='', verbose_name='Description about your guild')),
                ('tag', models.CharField(max_length=10, default='', verbose_name='Tag')),
                ('group_can_vote', models.ManyToManyField(to='auth.Group', related_name='group_can_vote', blank=True)),
                ('group_can_write_news', models.ManyToManyField(to='auth.Group', related_name='group_can_write_news', blank=True)),
                ('group_can_write_wiki', models.ManyToManyField(to='auth.Group', related_name='group_can_write_wiki', blank=True)),
=======
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guild_name', models.CharField(max_length=120, verbose_name='Guild name')),
                ('guild_motto', models.CharField(max_length=256, verbose_name='Guild motto')),
                ('short_guild_description', models.CharField(default=b'', max_length=120, verbose_name='Short description about your guild')),
                ('guild_description', models.TextField(default=b'', verbose_name='Description about your guild')),
                ('tag', models.CharField(default=b'', max_length=10, verbose_name='Tag')),
                ('group_can_vote', models.ManyToManyField(related_name='group_can_vote', to='auth.Group', blank=True)),
                ('group_can_write_news', models.ManyToManyField(related_name='group_can_write_news', to='auth.Group', blank=True)),
                ('group_can_write_wiki', models.ManyToManyField(related_name='group_can_write_wiki', to='auth.Group', blank=True)),
>>>>>>> 45c37a8a40bd684fb624e2710054e0a3ec0ba2bf
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
<<<<<<< HEAD
                ('id_uuid', models.CharField(editable=False, primary_key=True, max_length=36, default='9d796b34-7b88-49e8-b33a-634fb8b211ea', serialize=False)),
=======
                ('id_uuid', models.CharField(default=b'99300bd1-d17e-4c1d-8ab3-75d22380d61d', max_length=36, serialize=False, editable=False, primary_key=True)),
>>>>>>> 45c37a8a40bd684fb624e2710054e0a3ec0ba2bf
            ],
        ),
    ]
