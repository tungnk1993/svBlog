# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_auto_20151216_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='display_name',
            field=models.CharField(default=b'Test User Display Name', max_length=100),
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default=b'NoTitle', max_length=200),
        ),
    ]
