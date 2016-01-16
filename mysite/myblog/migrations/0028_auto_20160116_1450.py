# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0027_remove_vote_vote_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria_Optional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating_4',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating_5',
        ),
        migrations.AddField(
            model_name='review',
            name='optional_rating_1',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='optional_rating_2',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='optional_rating_3',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
