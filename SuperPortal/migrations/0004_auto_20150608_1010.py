# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('SuperPortal', '0003_auto_20150608_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildsettings',
            name='group_can_write_news',
            field=models.ManyToManyField(related_name='group_can_write_news', to='auth.Group', blank=True),
        ),
        migrations.AddField(
            model_name='guildsettings',
            name='group_can_write_wiki',
            field=models.ManyToManyField(related_name='group_can_write_wiki', to='auth.Group', blank=True),
        ),
        migrations.AlterField(
            model_name='guildsettings',
            name='group_can_vote',
            field=models.ManyToManyField(related_name='group_can_vote', to='auth.Group', blank=True),
        ),
        migrations.AlterField(
            model_name='superportal',
            name='id_uuid',
            field=models.CharField(default=b'924f85b1-8616-4bfe-9e5d-6f56ad102580', max_length=36, serialize=False, editable=False, primary_key=True),
        ),
    ]
