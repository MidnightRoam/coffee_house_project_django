# Generated by Django 3.2 on 2022-10-06 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_blog', '0009_auto_20221006_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 15, 54, 31, 266020)),
        ),
        migrations.DeleteModel(
            name='BlogComment',
        ),
    ]
