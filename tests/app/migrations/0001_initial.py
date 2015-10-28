# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('office', models.CharField(max_length=255, verbose_name='office')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
            ],
            options={
                'verbose_name': 'office',
                'verbose_name_plural': 'offices',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('name_de', models.CharField(max_length=255, verbose_name='name', null=True)),
                ('name_en', models.CharField(max_length=255, verbose_name='name', null=True)),
                ('surname', models.CharField(max_length=255, verbose_name='surname')),
                ('surname_de', models.CharField(max_length=255, verbose_name='surname', null=True)),
                ('surname_en', models.CharField(max_length=255, verbose_name='surname', null=True)),
                ('gender', models.CharField(max_length=255, choices=[('M', 'Male'), ('F', 'Female')], verbose_name='gender')),
                ('security_level', models.PositiveIntegerField(verbose_name='security level')),
                ('some_excluded_field', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='some decimal', null=True)),
                ('office', models.ForeignKey(blank=True, to='app.Office', null=True)),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='tag')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
    ]
