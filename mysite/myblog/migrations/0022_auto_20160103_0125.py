# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0021_auto_20151231_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='entity_subject',
        ),
        migrations.AddField(
            model_name='review',
            name='subject',
            field=models.TextField(default='Kinh te moi truong'),
            preserve_default=False,
        ),
    ]
