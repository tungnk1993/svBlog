# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0031_entity_edit_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity_edit_info',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
