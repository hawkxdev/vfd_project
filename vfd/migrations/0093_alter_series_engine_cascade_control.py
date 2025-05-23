# Generated by Django 4.0.6 on 2022-09-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0092_alter_series_engine_cascade_control'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='engine_cascade_control',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Нет'), (2, 'Да, 2 двигателя'), (3, 'Да, до 4 двигателей'), (4, 'Да, до 8 двигателей')], null=True, verbose_name='Управление каскадом двигателей'),
        ),
    ]
