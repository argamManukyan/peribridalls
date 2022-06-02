# Generated by Django 3.1 on 2022-06-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220602_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-my_order'], 'verbose_name': 'Բլոգ', 'verbose_name_plural': 'Բլոգ'},
        ),
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'ordering': ['-my_order'], 'verbose_name': 'Բլոգի բաժին', 'verbose_name_plural': 'Բլոգի բաժիններ'},
        ),
        migrations.AddField(
            model_name='blog',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Դասավորել'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Դասավորել'),
        ),
    ]
