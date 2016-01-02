# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0020_review_entity_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AlterField(
            model_name='entity',
            name='profile_pic',
            field=models.ImageField(default=b'default-user-image.jpg', upload_to=b''),
        ),
    ]
