# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0018_auto_20151230_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='entity',
            name='long_info',
        ),
        migrations.AddField(
            model_name='entity',
            name='subjects',
            field=models.ManyToManyField(to='myblog.Subject'),
        ),
    ]
