# Generated by Django 3.2 on 2022-09-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_blog', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_description',
            field=models.CharField(default='', max_length=250),
        ),
    ]
