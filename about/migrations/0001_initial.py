# Generated by Django 4.0.4 on 2022-05-30 12:37

import ckeditor_uploader.fields
import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text1', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='«Մեր մասին» առաջին հատված')),
                ('text1_hy', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='«Մեր մասին» առաջին հատված')),
                ('text1_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='«Մեր մասին» առաջին հատված')),
                ('text1_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='«Մեր մասին» առաջին հատված')),
                ('text2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='«Մեր մասին» երկրորդ հատված')),
                ('text2_hy', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='«Մեր մասին» երկրորդ հատված')),
                ('text2_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='«Մեր մասին» երկրորդ հատված')),
                ('text2_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='«Մեր մասին» երկրորդ հատված')),
            ],
            options={
                'verbose_name_plural': 'Մեր մասին',
            },
        ),
        migrations.CreateModel(
            name='AboutUsBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', core.utils.CustomLogoField(upload_to='')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Տեքստ')),
                ('text_hy', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Տեքստ')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Տեքստ')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Տեքստ')),
                ('url', models.CharField(max_length=1000)),
                ('url_hy', models.CharField(max_length=1000, null=True)),
                ('url_ru', models.CharField(max_length=1000, null=True)),
                ('url_en', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': '«Մեր մասին» բաններ',
            },
        ),
        migrations.CreateModel(
            name='AboutUsHomepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Տեքստ')),
                ('text_hy', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Տեքստ')),
                ('text_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Տեքստ')),
                ('text_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Տեքստ')),
                ('image', core.utils.CustomLogoField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Մեր մասին -ի գլխավոր էջի կոնտենտ',
            },
        ),
        migrations.CreateModel(
            name='OurAdvantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('icon', core.utils.CustomLogoField(blank=True, upload_to='')),
                ('name', models.CharField(max_length=255, verbose_name='Նպատակի անուն')),
                ('name_hy', models.CharField(max_length=255, null=True, verbose_name='Նպատակի անուն')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Նպատակի անուն')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Նպատակի անուն')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Նկարագրություն')),
                ('text_hy', models.TextField(blank=True, null=True, verbose_name='Նկարագրություն')),
                ('text_ru', models.TextField(blank=True, null=True, verbose_name='Նկարագրություն')),
                ('text_en', models.TextField(blank=True, null=True, verbose_name='Նկարագրություն')),
            ],
            options={
                'verbose_name': 'Առավելություն',
                'verbose_name_plural': 'Մեր առավելությունները',
            },
        ),
    ]
