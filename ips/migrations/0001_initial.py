# Generated by Django 4.0.6 on 2022-09-19 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0008_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpsSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplier.brand', verbose_name='Бренд')),
            ],
        ),
    ]
