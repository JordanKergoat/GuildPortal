# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Portal.models.news
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SuperPortal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('status', models.BooleanField(verbose_name='On holiday', default=False)),
                ('from_date', models.DateField(help_text='Please use the following format: DD-MM-YYYY', verbose_name='From')),
                ('to_date', models.DateField(help_text='Please use the following format: DD-MM-YYYY', verbose_name='to')),
                ('reason', models.TextField(help_text='You can explain why you are absent', verbose_name='Reason')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('main_character', models.BooleanField(help_text='You can specify if this character is your main', verbose_name='Main character', default=False)),
                ('level', models.SmallIntegerField(help_text='Specify your character level', blank=True, verbose_name='Character level', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterAttribute',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('attribute_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Class',
                'verbose_name': 'Class',
            },
        ),
        migrations.CreateModel(
            name='FieldValue',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('field_value', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('published_date', models.DateTimeField(verbose_name='Published date', auto_now_add=True)),
                ('modification_date', models.DateTimeField(null=True, blank=True, verbose_name='Modification date')),
                ('title', models.CharField(verbose_name='Title', max_length=100, primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='Body')),
                ('news_image', models.ImageField(verbose_name='News image', upload_to='/news/')),
                ('category', models.ForeignKey(help_text='News category', to='Portal.Category')),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'News',
                'verbose_name': 'News',
            },
        ),
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('active', models.BooleanField(verbose_name='Active ?', default=True)),
                ('name', models.CharField(verbose_name='Portal name', max_length=100)),
                ('guild_name', models.CharField(help_text='Can be blank. If blank, we will take guild name from SuperPortal', verbose_name='Portal guild name', max_length=100)),
                ('image', models.ImageField(verbose_name='Image', upload_to='/portal/logo/')),
                ('portal', models.ForeignKey(null=True, blank=True, to='SuperPortal.SuperPortal')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Tag', max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'verbose_name': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('birthday_date', models.DateField(verbose_name='Birthday date')),
                ('job_study', models.TextField(verbose_name='Job/Study')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Absent', 'Absent')], verbose_name='Member status', max_length=64)),
                ('country', models.CharField(verbose_name='Country', max_length=50)),
                ('town', models.CharField(verbose_name='Town', max_length=256)),
                ('teamspeak_nickname', models.CharField(verbose_name='TeamSpeak Nickname', blank=True, max_length=64)),
                ('mumble_nickname', models.CharField(verbose_name='Mumble Nickname', blank=True, max_length=64)),
                ('skype_nickname', models.CharField(verbose_name='Skype Nickname', blank=True, max_length=64)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(help_text='Tags list', to='Portal.Tag', db_constraint=Portal.models.news.Tag),
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
            field=models.ForeignKey(to='Portal.Game', default=''),
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
    ]
