# Generated by Django 3.0.5 on 2021-04-30 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210416_0122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nombreCategoria',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='imgPro1',
            new_name='imagen1',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='imgPro2',
            new_name='imagen2',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='imgPro3',
            new_name='imagen3',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='imgPro4',
            new_name='imagen4',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='imgPro5',
            new_name='imagen5',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombreProducto',
            new_name='nombre',
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(max_length=80, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Categoria'),
        ),
    ]