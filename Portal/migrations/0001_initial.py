# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import Portal.models.news


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
            name='FieldName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=64)),
            ],
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
                ('news_image', models.ImageField(upload_to=b'/news/', verbose_name='News image')),
                ('category', models.ForeignKey(help_text='News category', to='Portal.Category')),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
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
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(help_text='Tags list', db_constraint=Portal.models.news.Tag, to='Portal.Tag'),
        ),
        migrations.AddField(
            model_name='fieldname',
            name='field_value',
            field=models.ForeignKey(to='Portal.FieldValue'),
        ),
        migrations.AddField(
            model_name='fieldname',
            name='related_to',
            field=models.ForeignKey(to='Portal.Game'),
        ),
        migrations.AddField(
            model_name='class',
            name='game',
            field=models.ForeignKey(to='Portal.Game'),
        ),
    ]
