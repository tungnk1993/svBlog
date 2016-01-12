# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0026_auto_20160103_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='vote_value',
        ),
    ]
