# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0002_auto_20150603_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollement',
            name='game_choice',
        ),
        migrations.RemoveField(
            model_name='enrollement',
            name='user',
        ),
        migrations.DeleteModel(
            name='Enrollement',
        ),
    ]
