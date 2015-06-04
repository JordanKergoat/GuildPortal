# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('introduction', models.TextField()),
                ('character_name', models.CharField(max_length=50)),
                ('game_choice', models.ForeignKey(to='Portal.Game')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='FieldName',
            new_name='CharacterAttribute',
        ),
        migrations.RenameField(
            model_name='characterattribute',
            old_name='field_name',
            new_name='attribute_name',
        ),
        migrations.RenameField(
            model_name='characterattribute',
            old_name='field_value',
            new_name='attribute_value',
        ),
        migrations.RenameField(
            model_name='characterattribute',
            old_name='related_to',
            new_name='for_game',
        ),
    ]
