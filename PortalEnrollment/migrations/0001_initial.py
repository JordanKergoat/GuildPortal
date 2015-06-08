# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('introduction', models.TextField()),
                ('age', models.SmallIntegerField(verbose_name='Your age')),
                ('character_name', models.CharField(max_length=50)),
                ('another_characters', models.BooleanField(default=False, verbose_name='Another characters')),
                ('availability', models.TextField(verbose_name='Availabilities')),
                ('motivations', models.TextField(verbose_name='Motivations')),
                ('experience_PVE', models.TextField(verbose_name='Experiences PVE')),
                ('experience_PVP', models.TextField(verbose_name='Experiences PVP')),
                ('old_guild', models.TextField(verbose_name='Old Guilds')),
                ('game_choice', models.ForeignKey(to='Portal.Game')),
                ('roles', models.ManyToManyField(to='Portal.CharacterAttribute')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Enrollment',
                'verbose_name_plural': 'Enrollments',
            },
        ),
        migrations.CreateModel(
            name='EnrollmentSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('open', models.BooleanField(default=False, verbose_name='Open Enrollment')),
                ('limit', models.SmallIntegerField(verbose_name='Limit')),
                ('background_image', models.ImageField(upload_to=b'/enrollment/background/', verbose_name='Background image', blank=True)),
                ('thumbnail', models.ImageField(upload_to=b'/enrollment/thumbnail/', verbose_name='Thumbnail image', blank=True)),
                ('game_choice', models.ForeignKey(to='Portal.Game')),
                ('roles', models.ManyToManyField(to='Portal.CharacterAttribute')),
            ],
            options={
                'verbose_name': 'Enrollment settings',
                'verbose_name_plural': 'Enrollments settings',
            },
        ),
    ]
