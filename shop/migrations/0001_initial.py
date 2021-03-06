# Generated by Django 3.1 on 2022-06-02 11:09

import ckeditor_uploader.fields
import colorfield.fields
import core.utils
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_title_hy', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.TextField(blank=True, max_length=300, null=True)),
                ('meta_description_hy', models.TextField(blank=True, max_length=300, null=True)),
                ('meta_description_ru', models.TextField(blank=True, max_length=300, null=True)),
                ('meta_description_en', models.TextField(blank=True, max_length=300, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Անուն')),
                ('name_hy', models.CharField(max_length=255, null=True, verbose_name='Անուն')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Անուն')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Անուն')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Հղում')),
                ('image', core.utils.CustomLogoField(blank=True, null=True, upload_to='')),
                ('icon', core.utils.CustomLogoField(blank=True, null=True, upload_to='', verbose_name='Լոգո')),
                ('breadcrumb_image', core.utils.CustomLogoField(blank=True, null=True, upload_to='', verbose_name='Breadcrumb -ի նկար')),
                ('breadcrumb_text', models.TextField(blank=True, verbose_name='Breadcrumb -ի տեքստ')),
                ('breadcrumb_text_hy', models.TextField(blank=True, null=True, verbose_name='Breadcrumb -ի տեքստ')),
                ('breadcrumb_text_ru', models.TextField(blank=True, null=True, verbose_name='Breadcrumb -ի տեքստ')),
                ('breadcrumb_text_en', models.TextField(blank=True, null=True, verbose_name='Breadcrumb -ի տեքստ')),
            ],
            options={
                'verbose_name': 'Բրենդ',
                'verbose_name_plural': 'Բրենդներ',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_title_hy', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.TextField(blank=True, max_length=300, null=True)),
                ('meta_description_hy', models.TextField(blank=True, max_length=300, null=True)),
                ('meta_description_ru', models.TextField(blank=True, max_length=300, null=True)),
                ('meta_description_en', models.TextField(blank=True, max_length=300, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Անուն')),
                ('name_hy', models.CharField(max_length=255, null=True, verbose_name='Անուն')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Անուն')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Անուն')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Հղում')),
                ('image', core.utils.CustomLogoField(blank=True, null=True, upload_to='')),
                ('breadcrumb_image', core.utils.CustomLogoField(blank=True, null=True, upload_to='', verbose_name='Breadcrumb -ի նկար')),
                ('breadcrumb_text', models.TextField(blank=True, verbose_name='Breadcrumb -ի տեքստ')),
                ('breadcrumb_text_hy', models.TextField(blank=True, null=True, verbose_name='Breadcrumb -ի տեքստ')),
                ('breadcrumb_text_ru', models.TextField(blank=True, null=True, verbose_name='Breadcrumb -ի տեքստ')),
                ('breadcrumb_text_en', models.TextField(blank=True, null=True, verbose_name='Breadcrumb -ի տեքստ')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('mptt_level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='shop.category', verbose_name='Հայրական բաժին')),
            ],
            options={
                'verbose_name': 'Բաժին',
                'verbose_name_plural': 'Բաժիններ',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Գույնի անուն')),
                ('title_hy', models.CharField(max_length=255, null=True, verbose_name='Գույնի անուն')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Գույնի անուն')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Գույնի անուն')),
                ('color_code', colorfield.fields.ColorField(blank=True, default='#fff', image_field=None, max_length=18, null=True, samples=None, verbose_name='Գույնի կոդ')),
                ('my_order', models.PositiveIntegerField(default=0, verbose_name='Դասավորել')),
            ],
            options={
                'verbose_name': 'Գույն',
                'verbose_name_plural': 'Գույներ',
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='FilterField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_key', models.CharField(blank=True, editable=False, max_length=150, unique=True)),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Դաշտի անուն')),
                ('title_hy', models.CharField(max_length=255, null=True, unique=True, verbose_name='Դաշտի անուն')),
                ('title_ru', models.CharField(max_length=255, null=True, unique=True, verbose_name='Դաշտի անուն')),
                ('title_en', models.CharField(max_length=255, null=True, unique=True, verbose_name='Դաշտի անուն')),
                ('show_in_filters', models.BooleanField(default=False, verbose_name='Ցուցադրել ֆիլտրերում')),
                ('category', models.ManyToManyField(to='shop.Brand', verbose_name='Բրենդ')),
            ],
            options={
                'verbose_name': 'Ֆիլտրացման դաշտ',
                'verbose_name_plural': 'Ֆիլտրացման դաշտեր',
            },
        ),
        migrations.CreateModel(
            name='FilterValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Ֆիլտրացման արժեք')),
                ('title_hy', models.CharField(max_length=255, null=True, unique=True, verbose_name='Ֆիլտրացման արժեք')),
                ('title_ru', models.CharField(max_length=255, null=True, unique=True, verbose_name='Ֆիլտրացման արժեք')),
                ('title_en', models.CharField(max_length=255, null=True, unique=True, verbose_name='Ֆիլտրացման արժեք')),
            ],
            options={
                'verbose_name': 'Ֆիլտրվող արժեքներ',
                'verbose_name_plural': 'Ֆիլտրվեղ արժեքներ',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_title_hy', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.TextField(blank=True, max_length=300, null=True)),
                ('meta_description_hy', models.TextField(blank=True, max_length=300, null=True)),
                ('meta_description_ru', models.TextField(blank=True, max_length=300, null=True)),
                ('meta_description_en', models.TextField(blank=True, max_length=300, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Անուն')),
                ('name_hy', models.CharField(max_length=255, null=True, verbose_name='Անուն')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Անուն')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Անուն')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Հղում')),
                ('main_image', core.utils.CustomLogoField(upload_to='')),
                ('short_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Հակիրճ տեքստ')),
                ('short_text_hy', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Հակիրճ տեքստ')),
                ('short_text_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Հակիրճ տեքստ')),
                ('short_text_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Հակիրճ տեքստ')),
                ('large_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Ամբողջական տեքստ')),
                ('large_text_hy', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Ամբողջական տեքստ')),
                ('large_text_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Ամբողջական տեքստ')),
                ('large_text_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Ամբողջական տեքստ')),
                ('my_order', models.PositiveIntegerField(default=0, verbose_name='Դասավորել')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.brand', verbose_name='Բրենդ')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category', verbose_name='Բաժին')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.color', verbose_name='Գույն')),
            ],
            options={
                'verbose_name': 'Ապրանք',
                'verbose_name_plural': 'Ապրանքներ',
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', core.utils.CustomLogoField(upload_to='product-img/')),
                ('my_order', models.PositiveIntegerField(default=0, verbose_name='Դասավորել')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'verbose_name': 'Ապրանքի նկար',
                'verbose_name_plural': 'Ապրանքի նկարներ',
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('my_order', models.PositiveIntegerField(default=0, verbose_name='Դասավորել')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ակտիվ է')),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.filterfield', verbose_name='Դաշտ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Ապրանքի անուն')),
                ('value', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.filtervalue', verbose_name='Դաշտի արժեք')),
            ],
            options={
                'verbose_name': 'Ապրանքի չափորոշիչ',
                'verbose_name_plural': 'Ապրանքի չափորոշիչներ',
                'ordering': ['my_order'],
                'unique_together': {('product', 'field', 'value')},
            },
        ),
    ]
