# Generated by Django 4.2.2 on 2023-06-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_unibet', '0002_alter_partidas_time_casa_alter_partidas_time_fora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apostas',
            name='finalizada',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apostas',
            name='resultado',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]