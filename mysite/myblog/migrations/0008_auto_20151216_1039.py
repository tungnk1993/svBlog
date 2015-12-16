# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_auto_20151216_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_value', models.BooleanField()),
                ('vote_review', models.ForeignKey(related_name='vote_down_review', to='myblog.Review')),
                ('vote_user', models.ForeignKey(related_name='vote_up_user', to='myblog.MyUser')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='votedown',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='votedown',
            name='vote_review',
        ),
        migrations.RemoveField(
            model_name='votedown',
            name='vote_user',
        ),
        migrations.AlterUniqueTogether(
            name='voteup',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='voteup',
            name='vote_review',
        ),
        migrations.RemoveField(
            model_name='voteup',
            name='vote_user',
        ),
        migrations.DeleteModel(
            name='VoteDown',
        ),
        migrations.DeleteModel(
            name='VoteUp',
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('vote_user', 'vote_review')]),
        ),
    ]
