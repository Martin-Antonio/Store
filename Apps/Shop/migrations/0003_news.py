# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-04 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_shop_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
