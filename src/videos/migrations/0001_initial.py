# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('embed_code', models.TextField()),
            ],
        ),
    ]