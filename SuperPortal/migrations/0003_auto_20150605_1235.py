# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SuperPortal', '0002_auto_20150605_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildsettings',
            name='guild_description',
            field=models.TextField(default=b'', verbose_name='Description about your guild'),
        ),
        migrations.AddField(
            model_name='guildsettings',
            name='short_guild_description',
            field=models.CharField(default=b'', max_length=120, verbose_name='Short description about your guild'),
        ),
    ]
