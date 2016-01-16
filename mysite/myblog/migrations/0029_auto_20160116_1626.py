# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0028_auto_20160116_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='optional_rating_1',
            new_name='orating_1',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='optional_rating_2',
            new_name='orating_2',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='optional_rating_3',
            new_name='orating_3',
        ),
    ]
