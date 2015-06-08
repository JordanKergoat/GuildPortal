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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False, help_text=b'', verbose_name='On holiday')),
                ('from_date', models.DateField(help_text=b'Please use the following format: DD-MM-YYYY', verbose_name='From')),
                ('to_date', models.DateField(help_text=b'Please use the following format: DD-MM-YYYY', verbose_name='to')),
                ('reason', models.TextField(help_text=b'You can explain why you are absent', verbose_name='Reason')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_character', models.BooleanField(default=False, help_text=b'You can specify if this character is your main', verbose_name='Main character')),
                ('level', models.SmallIntegerField(default=0, help_text=b'Specify your character level', verbose_name='Character level', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribute_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Class',
            },
        ),
        migrations.CreateModel(
            name='CommentNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Published date')),
                ('content', models.TextField(default=b'', verbose_name='Your comment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FieldValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_value', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Published date')),
                ('modification_date', models.DateTimeField(null=True, verbose_name='Modification date', blank=True)),
                ('title', models.CharField(max_length=100, serialize=False, verbose_name='Title', primary_key=True)),
                ('content', models.TextField(verbose_name='Body')),
                ('news_image', models.ImageField(upload_to=b'news/', verbose_name='News image')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active ?')),
                ('name', models.CharField(max_length=100, verbose_name='Portal name')),
                ('guild_name', models.CharField(help_text=b'Can be blank. If blank, we will take guild name from SuperPortal', max_length=100, verbose_name='Portal guild name')),
                ('image', models.ImageField(upload_to=b'portal/logo/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
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
                ('games', models.ManyToManyField(to='Portal.Game', verbose_name='Games you play ?')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
