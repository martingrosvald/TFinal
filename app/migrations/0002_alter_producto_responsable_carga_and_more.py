# Generated by Django 4.0.5 on 2022-07-14 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='responsable_carga',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nro_celular',
            field=models.IntegerField(),
        ),
    ]