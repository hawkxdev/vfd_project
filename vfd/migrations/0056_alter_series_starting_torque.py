# Generated by Django 4.0.6 on 2022-09-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0055_alter_series_maximum_output_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='starting_torque',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '150% / 3 Гц'), (2, '160% / 0.5 Гц')], null=True, verbose_name='Пусковой момент (V/F)'),
        ),
    ]
