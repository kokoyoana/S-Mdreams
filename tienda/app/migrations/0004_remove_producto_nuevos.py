# Generated by Django 3.0.5 on 2021-04-08 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210408_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='nuevos',
        ),
    ]
