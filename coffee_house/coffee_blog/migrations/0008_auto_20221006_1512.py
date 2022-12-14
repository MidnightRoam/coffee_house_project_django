# Generated by Django 3.2 on 2022-10-06 13:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffee_blog', '0007_auto_20221006_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 6, 15, 12, 47, 309830)),
        ),
        migrations.CreateModel(
            name='BlogComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Message')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee_blog.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
