# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SuperPortal', '0002_auto_20150608_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superportal',
            name='id',
        ),
        migrations.AddField(
            model_name='superportal',
            name='id_uuid',
            field=models.CharField(default=b'9fe996b6-f0a5-4645-b468-c3a70a7459f8', max_length=36, serialize=False, editable=False, primary_key=True),
        ),
    ]
