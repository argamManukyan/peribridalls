# Generated by Django 3.2 on 2022-05-31 05:57

import core.utils
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20220530_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='breadcrumb_image',
            field=core.utils.CustomLogoField(blank=True, null=True, upload_to='', verbose_name='Breadcrumb -ի նկար'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='icon',
            field=core.utils.CustomLogoField(blank=True, null=True, upload_to='', verbose_name='Լոգո'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=core.utils.CustomLogoField(blank=True, null=True, upload_to=''),
        ),
    ]
