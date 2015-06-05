# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SuperPortal', '0003_auto_20150605_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperPortal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='guildsettings',
            name='tag',
            field=models.CharField(default=b'', max_length=10, verbose_name='Tag'),
        ),
    ]
