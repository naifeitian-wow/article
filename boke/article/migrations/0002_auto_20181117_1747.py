# Generated by Django 2.1.2 on 2018-11-17 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 17, 17, 47, 38, 132724), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='huifumodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 17, 17, 47, 38, 134723), verbose_name='回复时间'),
        ),
    ]