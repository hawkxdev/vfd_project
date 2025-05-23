# Generated by Django 4.0.6 on 2022-09-26 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0154_alter_series_power_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='control_panel',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, 'LED 4x7'), (20, 'LED 5x7'), (30, 'LED двухстрочный'), (31, 'LED 5x7 (LCD опционально)'), (32, 'LED двухстрочный (LCD опционально)'), (40, 'LCD дисплей')], null=True, verbose_name='Панель управления'),
        ),
        migrations.AlterField(
            model_name='series',
            name='copy_backup_settings',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (20, 'Да (LCD панель)'), (21, 'Да (только для дистанционного управления)'), (40, 'Да')], null=True, verbose_name='Копирование/бэкап настроек'),
        ),
        migrations.AlterField(
            model_name='series',
            name='inputs_outputs',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, 'DI: 4; AI: 1; TO: 0; RO: 1; AO: 1'), (20, 'DI: 4; AI: 2; TO: 0; RO: 1; AO: 1'), (30, 'DI: 5; AI: 1; TO: 1; RO: 1; AO: 1'), (40, 'DI: 6; AI: 2; TO: 0; RO: 1; AO: 1'), (41, 'DI: 5; AI: 2; TO: 1; RO: 1; AO: 1'), (50, 'DI: 6; AI: 2; TO: 1; RO: 2; AO: 2'), (60, 'DI: 7; AI: 2; TO: 3; RO: 1; AO: 1'), (61, 'DI: 7; AI: 2; TO: 2; RO: 2; AO: 1'), (62, 'DI: 8; AI: 2; TO: 2; RO: 1; AO: 1'), (70, 'DI: 7; AI: 3; TO: 2; RO: 1; AO: 2'), (80, 'DI: 10; AI: 3; TO: 0; RO: 3; AO: 2')], null=True, verbose_name='Входы/выходы'),
        ),
        migrations.AlterField(
            model_name='series',
            name='maximum_output_frequency',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, '320'), (20, '599; 90 кВт и выше: 400'), (21, '500'), (30, '599'), (31, '600'), (40, '999'), (50, '3000 (V/F); 300 (SVC)'), (51, '3200 (V/F); 300 (SVC)'), (52, '3200 (V/F); 500 (SVC)')], null=True, verbose_name='Максимальная выходная частота, Гц'),
        ),
        migrations.AlterField(
            model_name='series',
            name='starting_torque',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, '150% / 0.5 Гц'), (11, 'G type: 150% / 0.5 Гц (SVC)'), (12, 'G type: 150% / 0.5 Гц (SVC);\nP type: 100% / 0.5 Гц'), (13, '150% / 3 Гц (V/F), \n150% / 1 Гц (FVC)'), (14, '150% / 3 Гц (V/F, SVC для IM в тяжёлом режиме)\n100% / 2.5 Гц (V/F, SVC для PM в тяжёлом режиме)'), (15, '100% / 0.5 Гц (V/F); 150% / 0.5 Гц (SVC)'), (16, '150% / 3(1) Гц (V/F); 150% / 0.5 Гц (SVC)'), (17, 'G type: 150% / 0.5 Гц; \nP type: 100% / 0.5 Гц'), (18, 'Auto torque boost, manual torque boost 0.1%-30.0%; \nVector torque boost\t100-150'), (20, 'G type: 150% / 0.5 Гц (SVC), 180% / 0 Гц (VC);\nP type: 100% / 0.5 Гц')], null=True, verbose_name='Пусковой момент'),
        ),
    ]
