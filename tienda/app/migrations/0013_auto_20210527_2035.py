# Generated by Django 3.0.5 on 2021-05-27 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_producto_portada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tela',
            field=models.ForeignKey(max_length=80, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Tela'),
        ),
    ]
