# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0015_auto_20151222_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_written',
            field=models.DateField(auto_now_add=True),
        ),
    ]
