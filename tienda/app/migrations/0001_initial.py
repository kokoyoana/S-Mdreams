# Generated by Django 3.0.5 on 2021-04-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(null=True)),
                ('precio', models.IntegerField(null=True)),
                ('imgPro1', models.ImageField(upload_to='static/img')),
                ('imgPro2', models.ImageField(upload_to='static/img')),
                ('imgPro3', models.ImageField(upload_to='static/img')),
                ('imgPro4', models.ImageField(upload_to='static/img')),
                ('descripcion', models.TextField(max_length=10000, null=True)),
            ],
        ),
    ]
