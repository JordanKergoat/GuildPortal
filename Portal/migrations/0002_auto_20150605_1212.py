# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Portal name')),
                ('guild_name', models.CharField(help_text=b'Can be blank. If blank, we will take guild name from SuperPortal', max_length=100, verbose_name='Portal guild name')),
                ('image', models.ImageField(upload_to=b'/portal/logo/', verbose_name='Image')),
            ],
        ),
        migrations.RemoveField(
            model_name='guild',
            name='guild_chief',
        ),
        migrations.DeleteModel(
            name='Guild',
        ),
    ]
