# Generated by Django 3.2.6 on 2022-05-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='fecha',
            field=models.TimeField(),
        ),
    ]
