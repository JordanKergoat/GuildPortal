# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SuperPortal', '0004_auto_20150605_1256'),
        ('Portal', '0002_auto_20150605_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='portal',
            name='portal',
            field=models.ForeignKey(blank=True, to='SuperPortal.SuperPortal', null=True),
        ),
    ]
