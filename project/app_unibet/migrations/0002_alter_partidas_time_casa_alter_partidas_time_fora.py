# Generated by Django 4.2.2 on 2023-06-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_unibet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partidas',
            name='time_casa',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='partidas',
            name='time_fora',
            field=models.TextField(),
        ),
    ]