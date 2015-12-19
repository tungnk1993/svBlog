# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0013_auto_20151218_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=django_bleach.models.BleachField(),
        ),
    ]
