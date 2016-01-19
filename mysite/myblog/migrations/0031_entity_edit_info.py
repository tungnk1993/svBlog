# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0030_auto_20160116_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity_Edit_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('new_name', models.TextField(null=True, blank=True)),
                ('new_subject', models.TextField(null=True, blank=True)),
                ('new_info', models.TextField(null=True, blank=True)),
                ('new_profile_pic', models.TextField(null=True, blank=True)),
                ('contributor', models.ForeignKey(related_name='contributor', to='myblog.MyUser')),
                ('entity', models.ForeignKey(related_name='edit_entity', to='myblog.Entity')),
            ],
        ),
    ]
