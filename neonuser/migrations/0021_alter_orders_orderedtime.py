# Generated by Django 4.0.8 on 2022-11-28 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neonuser', '0020_alter_orders_orderedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderedtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 28, 13, 49, 25, 42038)),
        ),
    ]
