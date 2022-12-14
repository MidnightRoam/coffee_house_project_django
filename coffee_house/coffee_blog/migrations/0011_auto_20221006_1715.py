# Generated by Django 3.2 on 2022-10-06 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_blog', '0010_auto_20221006_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_description_en',
            field=models.CharField(default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='short_description_ru',
            field=models.CharField(default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_en',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_ru',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description_en',
            field=models.CharField(default='', max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description_ru',
            field=models.CharField(default='', max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='description_en',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='description_ru',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='name_en',
            field=models.CharField(max_length=64, null=True, verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='name_ru',
            field=models.CharField(max_length=64, null=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 17, 15, 8, 66251)),
        ),
    ]
