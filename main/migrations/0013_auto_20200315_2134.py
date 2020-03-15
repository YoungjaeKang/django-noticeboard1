# Generated by Django 3.0.3 on 2020-03-15 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200303_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(default=datetime.datetime(2020, 3, 15, 21, 34, 15, 602120), null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateField(default=datetime.datetime(2020, 3, 15, 21, 34, 15, 603078), null=True),
        ),
    ]