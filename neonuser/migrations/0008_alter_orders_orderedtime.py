# Generated by Django 4.0.4 on 2022-10-27 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neonuser', '0007_alter_orders_orderedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderedtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 27, 20, 30, 46, 270873)),
        ),
    ]