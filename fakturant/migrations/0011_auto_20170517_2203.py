# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 22:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakturant', '0010_auto_20170516_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='invoce_type',
            new_name='invoice_type',
        ),
    ]