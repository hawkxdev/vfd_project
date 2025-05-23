# Generated by Django 4.0.6 on 2022-09-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0049_alter_series_inputs_outputs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='motors',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'IM (асинхронные)'), (2, 'IM (асинхронные), PM (синхронные с постоянными магнитами)'), (3, 'IM (асинхронные), PM (синхронные с постоянными магнитами), SynRM (синхронные реактивные)')], null=True, verbose_name='Двигатели'),
        ),
    ]
