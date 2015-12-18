# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_auto_20151217_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='entity',
            name='is_teacher',
            field=models.BooleanField(default=True),
        ),
    ]
