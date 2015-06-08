# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absence',
            name='status',
            field=models.BooleanField(default=False, help_text=b'', verbose_name='On holiday'),
        ),
        migrations.AlterField(
            model_name='portal',
            name='image',
            field=models.ImageField(upload_to=b'portal/logo/', verbose_name='Image'),
        ),
    ]
