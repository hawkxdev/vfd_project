# Generated by Django 4.0.6 on 2022-09-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0061_alter_series_automatic_start_after_power_loss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='automatic_start_after_power_loss',
            field=models.BooleanField(blank=True, null=True, verbose_name='Автозапуск после пропадания питания'),
        ),
    ]
