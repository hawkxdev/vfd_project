# Generated by Django 4.0.6 on 2022-12-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0017_hmimodel_video_playback_from_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='hmimodel',
            name='vga_playback',
            field=models.BooleanField(blank=True, null=True, verbose_name='Воспроизведение по VGA с внешних устройств'),
        ),
    ]
