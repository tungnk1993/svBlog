# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0033_auto_20160119_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity_Add_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('subject', models.TextField(null=True, blank=True)),
                ('info', models.TextField(null=True, blank=True)),
                ('profile_pic', models.TextField(null=True, blank=True)),
                ('user_contact', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
