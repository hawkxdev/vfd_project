# Generated by Django 4.0.6 on 2022-12-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0003_alter_hmimodel_options_alter_hmiseries_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hmimodel',
            options={'ordering': ('series', 'article'), 'verbose_name': 'Модель', 'verbose_name_plural': 'Модели'},
        ),
        migrations.AddField(
            model_name='hmimodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка'),
        ),
    ]
