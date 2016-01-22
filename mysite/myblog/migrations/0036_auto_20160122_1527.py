# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0035_auto_20160121_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_icon',
            field=models.ImageField(default=b'images/default_user_icon.jpg', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(default=b'images/default_user_image.jpg', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='review',
            name='hidden_profile',
            field=models.ImageField(default=b'images/default-user-image.jpg', null=True, upload_to=b'', blank=True),
        ),
    ]
