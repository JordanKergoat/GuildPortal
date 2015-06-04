# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Portal', '0003_auto_20150604_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False, verbose_name='On holiday')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('reason', models.TextField(verbose_name='Reason')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roles', models.ManyToManyField(to='Portal.CharacterAttribute')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birthday_date', models.DateField(verbose_name='Birthday date')),
                ('job_study', models.TextField(verbose_name='Job/Study')),
                ('status', models.CharField(max_length=64, verbose_name='Member status', choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Absent', 'Absent')])),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('town', models.CharField(max_length=256, verbose_name='Town')),
                ('teamspeak_nickname', models.CharField(max_length=64, verbose_name='TeamSpeak Nickname', blank=True)),
                ('mumble_nickname', models.CharField(max_length=64, verbose_name='Mumble Nickname', blank=True)),
                ('skype_nickname', models.CharField(max_length=64, verbose_name='Skype Nickname', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
