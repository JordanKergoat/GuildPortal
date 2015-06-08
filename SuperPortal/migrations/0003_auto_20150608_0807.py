# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SuperPortal', '0002_auto_20150607_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superportal',
            name='id',
            field=models.CharField(default=b'818185bc-f724-403d-ae73-b5158d2a0c6d', max_length=36, serialize=False, editable=False, primary_key=True),
        ),
    ]
