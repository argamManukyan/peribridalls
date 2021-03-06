# Generated by Django 3.2 on 2022-06-01 09:49

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutusbanner',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Տեքստ'),
        ),
        migrations.AlterField(
            model_name='aboutusbanner',
            name='text_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Տեքստ'),
        ),
        migrations.AlterField(
            model_name='aboutusbanner',
            name='text_hy',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Տեքստ'),
        ),
        migrations.AlterField(
            model_name='aboutusbanner',
            name='text_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Տեքստ'),
        ),
        migrations.AlterField(
            model_name='aboutusbanner',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='aboutusbanner',
            name='url_en',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='aboutusbanner',
            name='url_hy',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='aboutusbanner',
            name='url_ru',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
