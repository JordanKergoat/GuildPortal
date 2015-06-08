# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('SuperPortal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guildsettings',
            name='group_can_vote',
        ),
        migrations.AddField(
            model_name='guildsettings',
            name='group_can_vote',
            field=models.ManyToManyField(to='auth.Group', blank=True),
        ),
        migrations.AlterField(
            model_name='superportal',
            name='id',
            field=models.CharField(default=b'41d40ae5-812a-49f8-937f-8259e4b6015c', max_length=36, serialize=False, editable=False, primary_key=True),
        ),
    ]
