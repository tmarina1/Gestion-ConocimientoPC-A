# Generated by Django 3.2.6 on 2022-05-19 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0002_alter_archivo_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
