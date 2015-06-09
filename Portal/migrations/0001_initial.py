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
            name='Absence',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('status', models.BooleanField(verbose_name='On holiday', default=False)),
                ('from_date', models.DateField(help_text='Please use the following format: DD-MM-YYYY', verbose_name='From')),
                ('to_date', models.DateField(help_text='Please use the following format: DD-MM-YYYY', verbose_name='to')),
                ('reason', models.TextField(help_text='You can explain why you are absent', verbose_name='Reason')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('main_character', models.BooleanField(help_text='You can specify if this character is your main', verbose_name='Main character', default=False)),
                ('level', models.SmallIntegerField(help_text='Specify your character level', verbose_name='Character level', default=0, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterAttribute',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('attribute_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Class',
                'verbose_name': 'Class',
            },
        ),
        migrations.CreateModel(
            name='CommentNews',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Published date')),
                ('content', models.TextField(default='', verbose_name='Your comment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FieldValue',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('field_value', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Games',
                'verbose_name': 'Game',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('published', models.BooleanField(verbose_name='Published', default=False)),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Published date')),
                ('modification_date', models.DateTimeField(null=True, blank=True, verbose_name='Modification date')),
                ('title', models.CharField(primary_key=True, max_length=100, verbose_name='Title', serialize=False)),
                ('content', models.TextField(verbose_name='Body')),
                ('news_image', models.ImageField(upload_to='news/', verbose_name='News image')),
            ],
            options={
                'verbose_name_plural': 'News',
                'verbose_name': 'News',
            },
        ),
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(verbose_name='Active ?', default=True)),
                ('name', models.CharField(max_length=100, verbose_name='Portal name')),
                ('guild_name', models.CharField(max_length=100, help_text='Can be blank. If blank, we will take guild name from SuperPortal', verbose_name='Portal guild name')),
                ('image', models.ImageField(upload_to='portal/logo/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='Tag')),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'verbose_name': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('birthday_date', models.DateField(verbose_name='Birthday date')),
                ('job_study', models.TextField(verbose_name='Job/Study')),
                ('status', models.CharField(max_length=64, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Absent', 'Absent')], verbose_name='Member status')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('town', models.CharField(max_length=256, verbose_name='Town')),
                ('teamspeak_nickname', models.CharField(max_length=64, blank=True, verbose_name='TeamSpeak Nickname')),
                ('mumble_nickname', models.CharField(max_length=64, blank=True, verbose_name='Mumble Nickname')),
                ('skype_nickname', models.CharField(max_length=64, blank=True, verbose_name='Skype Nickname')),
                ('games', models.ManyToManyField(to='Portal.Game', verbose_name='Games you play ?')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
