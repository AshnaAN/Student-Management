# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Front',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('clss', models.CharField(max_length=6)),
                ('mark1', models.IntegerField()),
                ('mark2', models.IntegerField()),
                ('mark3', models.IntegerField()),
                ('rollno', models.IntegerField()),
            ],
        ),
    ]
