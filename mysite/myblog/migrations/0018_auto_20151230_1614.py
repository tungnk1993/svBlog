# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0017_auto_20151230_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='profile_icon',
            field=models.ImageField(default=b'default_user_icon.jpg', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(default=b'default_user_image.jpg', upload_to=b''),
        ),
    ]
