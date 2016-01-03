# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0024_review_is_fake'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
