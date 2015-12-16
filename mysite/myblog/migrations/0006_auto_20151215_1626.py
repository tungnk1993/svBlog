# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20151215_1610'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('author', 'entity')]),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('vote_user', 'vote_review')]),
        ),
    ]
