# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakturant', '0006_auto_20170516_1940'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientCompany',
            new_name='Company',
        ),
    ]