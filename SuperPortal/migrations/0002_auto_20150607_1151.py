# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SuperPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superportal',
            name='id',
            field=models.CharField(default=b'6c848209-ffd9-4758-8cc3-694f8bd87a0c', max_length=36, serialize=False, editable=False, primary_key=True),
        ),
    ]
