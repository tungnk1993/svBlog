# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20151215_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='profile_pic',
            field=models.ImageField(default=b'default-user-image.png', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(default=b'default-user-image.png', upload_to=b''),
        ),
    ]
