# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0032_auto_20160119_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity_edit_info',
            name='contributor',
        ),
        migrations.AddField(
            model_name='entity_edit_info',
            name='user_contact',
            field=models.TextField(null=True, blank=True),
        ),
    ]
