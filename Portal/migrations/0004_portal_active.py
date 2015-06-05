# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0003_portal_portal'),
    ]

    operations = [
        migrations.AddField(
            model_name='portal',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active ?'),
        ),
    ]
