# Generated by Django 3.0.5 on 2021-04-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_producto_nuevos'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imgPro5',
            field=models.ImageField(default=1, upload_to='static/img'),
            preserve_default=False,
        ),
    ]
