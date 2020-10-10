# Generated by Django 3.1.2 on 2020-10-10 02:34

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 11, 2, 34, 6, 62559)),
        ),
    ]
