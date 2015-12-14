# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('short_info', models.TextField()),
                ('long_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_pic', models.ImageField(upload_to=b'')),
                ('short_bio', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_written', models.DateField()),
                ('content', models.TextField()),
                ('rating_overall', models.IntegerField()),
                ('rating_1', models.IntegerField()),
                ('rating_2', models.IntegerField()),
                ('rating_3', models.IntegerField()),
                ('rating_4', models.IntegerField()),
                ('rating_5', models.IntegerField()),
                ('tag_1', models.IntegerField()),
                ('tag_2', models.IntegerField()),
                ('tag_3', models.IntegerField()),
                ('tag_4', models.IntegerField()),
                ('tag_5', models.IntegerField()),
                ('author', models.ForeignKey(related_name='author', to='myblog.MyUser')),
                ('entity', models.ForeignKey(related_name='entity', to='myblog.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_value', models.BooleanField()),
                ('vote_review', models.ForeignKey(related_name='vote_review', to='myblog.Review')),
                ('vote_user', models.ForeignKey(related_name='vote_user', to='myblog.MyUser')),
            ],
        ),
    ]
