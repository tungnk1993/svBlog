# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20151215_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteDown',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_review', models.ForeignKey(related_name='vote_review', to='myblog.Review')),
                ('vote_user', models.ForeignKey(related_name='vote_user', to='myblog.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='VoteUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_review', models.ForeignKey(related_name='vote_down_review', to='myblog.Review')),
                ('vote_user', models.ForeignKey(related_name='vote_up_user', to='myblog.MyUser')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_review',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_user',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
        migrations.AlterUniqueTogether(
            name='voteup',
            unique_together=set([('vote_user', 'vote_review')]),
        ),
        migrations.AlterUniqueTogether(
            name='votedown',
            unique_together=set([('vote_user', 'vote_review')]),
        ),
    ]
