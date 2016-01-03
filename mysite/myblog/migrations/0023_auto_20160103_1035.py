# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0022_auto_20160103_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='hidden_bio',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='hidden_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='hidden_profile',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
