# Generated by Django 4.0.6 on 2022-10-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0178_series_case_quality_alter_series_control_panel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='installation_connection',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(30, 'Удобные клеммники и маркировка;'), (40, 'Удобные клеммники и маркировка; отверстия-капли для крепления')], null=True, verbose_name='Удобство монтажа и подключения'),
        ),
        migrations.AlterField(
            model_name='series',
            name='case_quality',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, 'Прочный корпус; неудобное снятие клеммной крышки, дребезжит крышка вентилятора'), (30, 'Прочный корпус, качественная сборка; чёрный матовый, не вонючий пластик'), (31, 'Прочный корпус, качественная сборка')], null=True, verbose_name='Качество корпуса'),
        ),
        migrations.AlterField(
            model_name='series',
            name='minimum_size',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(30, '212x95x154'), (40, '202x70x161'), (50, '170x78x134'), (41, '176x90x145'), (31, '186x125x170')], null=True, verbose_name='Минимальный габарит, ВхШхГ'),
        ),
        migrations.AlterField(
            model_name='series',
            name='starting_torque',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, '150% / 0.5 Гц'), (11, 'G type: 150% / 0.5 Гц (SVC)'), (12, 'G type: 150% / 0.5 Гц (SVC);\nP type: 100% / 0.5 Гц'), (13, '150% / 3 Гц (V/F), \n150% / 1 Гц (FVC)'), (14, '150% / 3 Гц (V/F, SVC для IM в тяжёлом режиме)\n100% / 2.5 Гц (V/F, SVC для PM в тяжёлом режиме)'), (15, '100% / 0.5 Гц (V/F); 150% / 0.5 Гц (SVC)'), (16, '150% / 3(1) Гц (V/F); 150% / 0.5 Гц (SVC)'), (17, 'G type: 150% / 0.5 Гц; \nP type: 100% / 0.5 Гц'), (18, 'Auto torque boost, manual torque boost 0.1%-30%; Vector torque boost 100-150; Start frequency 0.4Hz-20Hz'), (19, '150% / 0.5 Гц (SVC)'), (20, 'G type: 150% / 0.5 Гц (SVC), 180% / 0 Гц (VC);\nP type: 100% / 0.5 Гц'), (21, 'Auto torque boost, manual torque boost 0.1%-30%; Cut-off frequency of torque boost 0Hz to maximum output frequency'), (22, 'До 180% от номинального (Функция намагничивания постоянным током)')], null=True, verbose_name='Пусковой момент'),
        ),
    ]
