# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0029_auto_20160116_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='orating_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='orating_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='orating_3',
            field=models.IntegerField(default=0),
        ),
    ]
