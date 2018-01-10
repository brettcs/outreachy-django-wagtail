# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-09 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_auto_20180109_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='communication_help',
            field=models.URLField(blank=True, help_text='(Optional) URL for the user documentation for your communication protocol'),
        ),
        migrations.AddField(
            model_name='project',
            name='communication_tool',
            field=models.CharField(blank=True, help_text='(Optional) Which communication tool does your project use? E.g. IRC, Zulip, Discourse, etc.', max_length=100),
        ),
    ]