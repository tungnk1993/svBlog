# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0034_entity_add_info'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subject',
            unique_together=set([('name',)]),
        ),
    ]
