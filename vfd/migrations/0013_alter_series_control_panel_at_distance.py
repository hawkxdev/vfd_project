# Generated by Django 4.0.6 on 2022-09-14 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0012_alter_series_control_panel_at_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='control_panel_at_distance',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (1, 'Да, при помощи кабеля-аксессуара'), (2, 'Да, соединение обычным патч-кордом')], max_length=200, null=True, verbose_name='Выносной пульт'),
        ),
    ]
