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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('status', models.BooleanField(verbose_name='On holiday', default=False)),
                ('from_date', models.DateField(verbose_name='From', help_text='Please use the following format: DD-MM-YYYY')),
                ('to_date', models.DateField(verbose_name='to', help_text='Please use the following format: DD-MM-YYYY')),
                ('reason', models.TextField(verbose_name='Reason', help_text='You can explain why you are absent')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('main_character', models.BooleanField(verbose_name='Main character', default=False, help_text='You can specify if this character is your main')),
                ('level', models.SmallIntegerField(verbose_name='Character level', blank=True, default=0, help_text='Specify your character level')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('attribute_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Class',
            },
        ),
        migrations.CreateModel(
            name='FieldValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('field_value', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('published', models.BooleanField(verbose_name='Published', default=False)),
                ('published_date', models.DateTimeField(verbose_name='Published date', auto_now_add=True)),
                ('modification_date', models.DateTimeField(verbose_name='Modification date', blank=True, null=True)),
                ('title', models.CharField(verbose_name='Title', max_length=100, primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='Body')),
                ('news_image', models.ImageField(verbose_name='News image', upload_to='news/')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('active', models.BooleanField(verbose_name='Active ?', default=True)),
                ('name', models.CharField(verbose_name='Portal name', max_length=100)),
                ('guild_name', models.CharField(verbose_name='Portal guild name', help_text='Can be blank. If blank, we will take guild name from SuperPortal', max_length=100)),
                ('image', models.ImageField(verbose_name='Image', upload_to='portal/logo/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Tag', max_length=64)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('birthday_date', models.DateField(verbose_name='Birthday date')),
                ('job_study', models.TextField(verbose_name='Job/Study')),
                ('status', models.CharField(verbose_name='Member status', max_length=64, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Absent', 'Absent')])),
                ('country', models.CharField(verbose_name='Country', max_length=50)),
                ('town', models.CharField(verbose_name='Town', max_length=256)),
                ('teamspeak_nickname', models.CharField(verbose_name='TeamSpeak Nickname', blank=True, max_length=64)),
                ('mumble_nickname', models.CharField(verbose_name='Mumble Nickname', blank=True, max_length=64)),
                ('skype_nickname', models.CharField(verbose_name='Skype Nickname', blank=True, max_length=64)),
                ('games', models.ManyToManyField(verbose_name='Games you play ?', to='Portal.Game')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
