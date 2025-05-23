# Generated by Django 4.0.6 on 2022-09-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0114_alter_series_maximum_output_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='maximum_output_frequency',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, '320'), (20, '599; 90 кВт и выше: 400'), (30, '599'), (40, '999'), (50, '3000 (V/F); 300 (SVC)')], null=True, verbose_name='Максимальная выходная частота, Гц'),
        ),
    ]
