# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-08 17:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nit',
            field=models.DecimalField(decimal_places=0, max_digits=11),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='latitud',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='longitud',
            field=models.IntegerField(unique=True),
        ),
    ]
