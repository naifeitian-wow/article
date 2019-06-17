# Generated by Django 2.1.2 on 2018-11-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfomodel',
            name='nick',
            field=models.CharField(max_length=30, null=True, verbose_name='昵称'),
        ),
        migrations.AddField(
            model_name='userinfomodel',
            name='touxiang',
            field=models.ImageField(default=123, upload_to='static/images/pic', verbose_name='头像'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=20, verbose_name='用户名'),
        ),
    ]
