# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0002_auto_20150607_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='portal',
            field=models.ForeignKey(default=1, verbose_name='Publish on which portal ?', to='Portal.Portal'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(verbose_name='Select categories', to='Portal.Category', help_text='News category'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=models.ImageField(upload_to=b'news/', verbose_name='News image'),
        ),
    ]
