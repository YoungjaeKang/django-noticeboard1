# Generated by Django 3.0.3 on 2020-02-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200218_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
