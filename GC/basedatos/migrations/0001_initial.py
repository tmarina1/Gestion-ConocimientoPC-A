# Generated by Django 3.2.6 on 2022-05-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('fecha', models.TimeField(auto_now_add=True)),
                ('archivo', models.FileField(upload_to='archivos/')),
            ],
        ),
    ]
