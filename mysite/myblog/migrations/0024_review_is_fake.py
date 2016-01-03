# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0023_auto_20160103_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_fake',
            field=models.BooleanField(default=False),
        ),
    ]
