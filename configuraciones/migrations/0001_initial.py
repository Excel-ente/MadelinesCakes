# Generated by Django 3.2.18 on 2023-04-30 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rutas_Descarga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=50)),
                ('RUTA_DESCARGA', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'Variable',
                'verbose_name_plural': 'Variables',
            },
        ),
    ]