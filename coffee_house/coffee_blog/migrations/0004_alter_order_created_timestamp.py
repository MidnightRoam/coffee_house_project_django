# Generated by Django 3.2 on 2022-10-05 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_blog', '0003_alter_order_created_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 5, 12, 7, 13, 772310)),
        ),
    ]
