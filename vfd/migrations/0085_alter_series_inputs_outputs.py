# Generated by Django 4.0.6 on 2022-09-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0084_alter_series_inputs_outputs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='inputs_outputs',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'DI: 4; AI: 1; TO: 0; RO: 1; AO: 1'), (2, 'DI: 4; AI: 2; TO: 0; RO: 1; AO: 1'), (3, 'DI: 6; AI: 2; TO: 0; RO: 1; AO: 1'), (4, 'DI: 6; AI: 2; TO: 1; RO: 2; AO: 2'), (5, 'DI: 7; AI: 2; TO: 3; RO: 1; AO: 1'), (6, 'DI: 10; AI: 3; TO: 0; RO: 3; AO: 2')], null=True, verbose_name='Входы/выходы'),
        ),
    ]
