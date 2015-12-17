# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_auto_20151217_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='display_name',
            new_name='name',
        ),
    ]
