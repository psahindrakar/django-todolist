# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 14:52
from __future__ import unicode_literals

import company.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20160907_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='insurance_file',
            field=models.FileField(blank=True, default='', upload_to=company.models.company_file_storage_path),
        ),
    ]