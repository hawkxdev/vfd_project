# Generated by Django 4.0.6 on 2022-09-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0162_alter_series_inputs_outputs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='carrier_frequency',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(31, '2...15'), (32, '2...15 (Default: 4)'), (33, '2...15/10/9 (Default: 8/6/4)'), (34, '2...16 (Default: 4/3)'), (35, '1...16/10/5 (Default: 6/4.5/3/1.8)'), (36, '2...12 (Default: 3)'), (37, '1...14 (Default: 8)'), (38, '1...15 (Default: 8/4/2)'), (40, '0.5...16')], null=True, verbose_name='Несущая частота ШИМ, кГц'),
        ),
        migrations.AlterField(
            model_name='series',
            name='choke_dc_link',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (10, 'Опция от 75кВт'), (20, 'Опция 45...400кВт, встроен от 450кВт'), (30, 'Опция'), (40, 'Встроен на мощности 11, 15 кВт и от 200 кВт'), (50, 'Встроен на мощности от 45 кВт'), (60, 'Встроен на мощности от 37 кВт'), (90, 'Встроен')], null=True, verbose_name='Дроссель в звене постоянного тока'),
        ),
    ]
