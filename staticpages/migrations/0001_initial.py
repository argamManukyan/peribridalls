# Generated by Django 3.2 on 2022-06-02 05:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('page_title', models.CharField(max_length=160, verbose_name='Էջի վերնագիր')),
                ('page_title_hy', models.CharField(max_length=160, null=True, verbose_name='Էջի վերնագիր')),
                ('page_title_ru', models.CharField(max_length=160, null=True, verbose_name='Էջի վերնագիր')),
                ('page_title_en', models.CharField(max_length=160, null=True, verbose_name='Էջի վերնագիր')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Տեքստ')),
                ('text_hy', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Տեքստ')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Տեքստ')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Տեքստ')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='Հղում')),
                ('my_order', models.PositiveIntegerField(default=0, verbose_name='Դասավորել')),
            ],
            options={
                'verbose_name': 'Ստատիկ էջ',
                'verbose_name_plural': 'Ստատիկ էջեր',
                'ordering': ['my_order'],
            },
        ),
    ]
