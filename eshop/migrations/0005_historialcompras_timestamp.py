# Generated by Django 2.1.5 on 2019-04-07 22:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0004_historialcompras'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialcompras',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 22, 38, 11, 350560, tzinfo=utc)),
        ),
    ]
