# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0025_review_is_anonymous'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='content',
            new_name='content_study',
        ),
        migrations.AddField(
            model_name='review',
            name='content_teacher',
            field=django_bleach.models.BleachField(default='Default value'),
            preserve_default=False,
        ),
    ]
