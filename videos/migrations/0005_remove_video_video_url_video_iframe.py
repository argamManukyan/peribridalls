# Generated by Django 4.0 on 2022-07-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_video_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_url',
        ),
        migrations.AddField(
            model_name='video',
            name='iframe',
            field=models.TextField(blank=True, verbose_name='Տեսահոլովակի iframe'),
        ),
    ]