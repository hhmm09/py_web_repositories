# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-20 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20190217_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursesorg',
            old_name='image',
            new_name='adress',
        ),
    ]
