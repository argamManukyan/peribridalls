# Generated by Django 3.1 on 2022-06-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20220602_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['my_order'], 'verbose_name': 'Տեսահոլովակ', 'verbose_name_plural': 'Տեսահոլովակ'},
        ),
        migrations.AddField(
            model_name='video',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Դասավորել'),
        ),
    ]