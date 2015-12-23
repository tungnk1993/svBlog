# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0014_auto_20151219_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='tag_1',
            field=models.ForeignKey(related_name='tag1', blank=True, to='myblog.Tag', null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='tag_2',
            field=models.ForeignKey(related_name='tag2', blank=True, to='myblog.Tag', null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='tag_3',
            field=models.ForeignKey(related_name='tag3', blank=True, to='myblog.Tag', null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='tag_4',
            field=models.ForeignKey(related_name='tag4', blank=True, to='myblog.Tag', null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='tag_5',
            field=models.ForeignKey(related_name='tag5', blank=True, to='myblog.Tag', null=True),
        ),
    ]
