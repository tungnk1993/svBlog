# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0011_criteria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria_Uni',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Criteria',
            new_name='Criteria_Teacher',
        ),
        migrations.AddField(
            model_name='review',
            name='is_teacher',
            field=models.BooleanField(default=True),
        ),
    ]
