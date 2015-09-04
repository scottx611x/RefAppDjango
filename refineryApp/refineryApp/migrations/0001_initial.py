# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('category_name', models.CharField(max_length=120)),
                ('category_Description', models.CharField(max_length=300)),
                ('date_Created', models.DateTimeField(auto_now_add=True)),
                ('last_Modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('workflow_name', models.CharField(max_length=120)),
                ('workflow_Description', models.CharField(max_length=300)),
                ('workflow_Steps', models.IntegerField()),
                ('date_Created', models.DateTimeField(auto_now_add=True)),
                ('last_Modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(to='refineryApp.Category')),
            ],
        ),
    ]
