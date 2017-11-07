# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 13:15
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pulse', '0002_auto_20171013_1139'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=255)),
                ('deck', models.TextField(blank=True, max_length=1020)),
                ('deck_html', models.TextField(blank=True, editable=False)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Publication date')),
                ('entries', models.ManyToManyField(blank=True, db_table='r_Collection_Entries', to='pulse.Entry')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pulse.Media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Collections',
                'db_table': 'r_Collection',
                'ordering': ['-pub_date'],
                'get_latest_by': 'pub_date',
            },
        ),
        migrations.CreateModel(
            name='Promoted',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=255)),
                ('deck', models.TextField(blank=True, max_length=1020)),
                ('deck_html', models.TextField(blank=True, editable=False)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Publication date')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulse.Entry')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pulse.Media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promoted_entries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Promoted Entries',
                'db_table': 'r_Promoted',
                'ordering': ['-pub_date'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]
