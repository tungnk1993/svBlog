# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0019_auto_20151231_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='entity_subject',
            field=models.ForeignKey(related_name='entity_subject', default=6, to='myblog.Subject'),
        ),
    ]
