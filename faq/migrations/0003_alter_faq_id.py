# Generated by Django 4.0 on 2022-06-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20220602_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
