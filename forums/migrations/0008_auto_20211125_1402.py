# Generated by Django 3.2.9 on 2021-11-25 06:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0007_auto_20211125_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 25, 14, 2, 43), null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 25, 14, 2, 43), null=True),
        ),
    ]
