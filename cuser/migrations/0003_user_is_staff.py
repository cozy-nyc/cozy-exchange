# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuser', '0002_user_email_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='active'),
        ),
    ]
