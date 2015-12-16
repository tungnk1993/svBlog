# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_remove_review_rating_overall'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='profile_pic',
            field=models.ImageField(default=b'static/default-user-image.png', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(default=b'static/default-user-image.png', upload_to=b''),
        ),
    ]
