# Generated by Django 4.0.6 on 2022-09-13 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0002_alter_series_emc_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='pulse_frequency_setting',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (1, 'Да')], null=True, verbose_name='Импульсное задание частоты'),
        ),
    ]
